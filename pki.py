#!/bin/env python3
# -*- coding: utf-8 -*-

import os
import random

from OpenSSL import crypto

def make_self_signed_ca(cert_path,
                        private_key: crypto.PKey = None,
                        certificate: crypto.X509 = None):
    """
    Use OpenSSL to create a new Cert and Key
    """
    if cert_path is not None and os.path.isfile(cert_path):
        return False

    # create a key pair
    if not private_key:
        private_key = crypto.PKey()
        private_key.generate_key(crypto.TYPE_RSA, 4096)

    # create a self-signed certificate
    if not certificate:
        certificate = crypto.X509()
        subject = certificate.get_subject()
        subject.C = "SE"
        subject.ST = "Example State"
        subject.OU = "Example Organization"
        subject.CN = "localhost"

        # Valid from now
        certificate.gmtime_adj_notBefore(0)

        # Expire certificate after 1 year
        certificate.gmtime_adj_notAfter(365 * 24 * 60 * 60)
        certificate.set_issuer(certificate.get_subject())
        certificate.set_pubkey(private_key)

    # Use a unique serial number
    certificate.set_serial_number(random.randint(1, 2147483647))
    certificate.sign(private_key, "sha256")

    cert_pem = crypto.dump_certificate(
        crypto.FILETYPE_PEM,
        certificate).decode()
    key_pem = crypto.dump_privatekey(
        crypto.FILETYPE_PEM,
        private_key).decode()

    with open(cert_path, "w") as f:
        f.write(key_pem)
        f.write(cert_pem)

    return True
