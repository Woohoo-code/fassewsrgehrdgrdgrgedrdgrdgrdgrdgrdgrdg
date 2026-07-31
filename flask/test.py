from cryptography import x509
from cryptography.x509.oid import NameOID
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import rsa

from datetime import datetime, timedelta, UTC
import ipaddress


# CHANGE THIS TO YOUR SERVER IP
SERVER_IP = "10.144.6.57"


def make_key():
    return rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048
    )


def save_key(key, filename):
    with open(filename, "wb") as f:
        f.write(
            key.private_bytes(
                serialization.Encoding.PEM,
                serialization.PrivateFormat.TraditionalOpenSSL,
                serialization.NoEncryption()
            )
        )


# -------------------------
# Create Certificate Authority
# -------------------------

ca_key = make_key()

ca_name = x509.Name([
    x509.NameAttribute(
        NameOID.ORGANIZATION_NAME,
        "My LAN Certificate Authority"
    ),
    x509.NameAttribute(
        NameOID.COMMON_NAME,
        "My LAN Root CA"
    ),
])


ca_cert = (
    x509.CertificateBuilder()
    .subject_name(ca_name)
    .issuer_name(ca_name)
    .public_key(ca_key.public_key())
    .serial_number(x509.random_serial_number())
    .not_valid_before(datetime.now(UTC))
    .not_valid_after(
        datetime.now(UTC) + timedelta(days=3650)
    )
    .add_extension(
        x509.BasicConstraints(
            ca=True,
            path_length=None
        ),
        critical=True
    )
    .sign(
        ca_key,
        hashes.SHA256()
    )
)


save_key(ca_key, "lan_ca_key.pem")

with open("lan_ca_cert.pem", "wb") as f:
    f.write(
        ca_cert.public_bytes(
            serialization.Encoding.PEM
        )
    )


# -------------------------
# Create Server Certificate
# -------------------------

server_key = make_key()

server_name = x509.Name([
    x509.NameAttribute(
        NameOID.COMMON_NAME,
        SERVER_IP
    )
])


server_cert = (
    x509.CertificateBuilder()
    .subject_name(server_name)
    .issuer_name(ca_cert.subject)
    .public_key(server_key.public_key())
    .serial_number(x509.random_serial_number())
    .not_valid_before(datetime.now(UTC))
    .not_valid_after(
        datetime.now(UTC) + timedelta(days=825)
    )
    .add_extension(
        x509.SubjectAlternativeName([
            x509.IPAddress(
                ipaddress.IPv4Address(SERVER_IP)
            ),
            x509.DNSName("localhost")
        ]),
        critical=False
    )
    .sign(
        ca_key,
        hashes.SHA256()
    )
)


save_key(server_key, "server_key.pem")

with open("server_cert.pem", "wb") as f:
    f.write(
        server_cert.public_bytes(
            serialization.Encoding.PEM
        )
    )


print("Created:")
print("  lan_ca_cert.pem  <- install this as trusted")
print("  server_cert.pem  <- use in your server")
print("  server_key.pem   <- use in your server")