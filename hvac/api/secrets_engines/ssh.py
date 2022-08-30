#!/usr/bin/env python
"""SSH vault secrets backend module."""

from hvac import utils
from hvac.api.vault_api_base import VaultApiBase

DEFAULT_MOUNT_POINT = "ssh"

# TODO Fix return types for GET and LIST API calls


class Ssh(VaultApiBase):
    """SSH Secrets Engine (API).
    Reference: https://www.vaultproject.io/api-docs/secret/ssh
    """

    async def create_or_update_key(
        self,
        name="",
        key="",
        mount_point=DEFAULT_MOUNT_POINT,
    ):
        """This endpoint updates a named key.

        :param name: Specifies the name of the key to create.
        :type name: str | unicode
        :param key: Specifies an SSH private key with appropriate privileges on remote hosts.
        :type key: str | unicode
        :param mount_point: Specifies the place where the secrets engine will be accessible (default: ssh).
        :type mount_point: str | unicode
        :return: The JSON response of the request
        :rtype: aiohttp.ClientResponse
        """
        params = {
            "key": key,
        }

        api_path = utils.format_url(
            "/v1/{mount_point}/keys/{name}",
            mount_point=mount_point,
            name=name,
        )

        return await self._adapter.post(
            url=api_path,
            json=params,
        )

    async def delete_key(
        self,
        name="",
        mount_point=DEFAULT_MOUNT_POINT,
    ):
        """This endpoint deletes a named key.

        :param name: Specifies the name of the key to delete.
        :type name: str | unicode
        :param mount_point: Specifies the place where the secrets engine will be accessible (default: ssh).
        :type mount_point: str | unicode
        :return: The JSON response of the request
        :rtype: aiohttp.ClientResponse
        """
        api_path = utils.format_url(
            "/v1/{mount_point}/keys/{name}",
            mount_point=mount_point,
            name=name,
        )

        return await self._adapter.delete(url=api_path)

    async def create_role(
        self,
        name="",
        key="",
        admin_user="",
        default_user="",
        cidr_list="",
        exclude_cidr_list="",
        port=22,
        key_type="",
        key_bits=1024,
        install_script="",
        allowed_users="",
        allowed_users_template="",
        allowed_domains="",
        key_option_specs="",
        ttl="",
        max_ttl="",
        allowed_critical_options="",
        allowed_extensions="",
        default_critical_options=None,
        default_extensions=None,
        allow_user_certificates="",
        allow_host_certificates=False,
        allow_bare_domains=False,
        allow_subdomains=False,
        allow_user_key_ids=False,
        key_id_format="",
        allowed_user_key_lengths=None,
        algorithm_signer="",
        mount_point=DEFAULT_MOUNT_POINT,
    ):
        """This endpoint creates or updates a named role.

        :param name: Specifies the name of the role to create.
        :type name: str | unicode
        :param key: Specifies the name of the registered key in Vault.
        :type key: str | unicode
        :param admin_user: Specifies the admin user at remote host.
        :type admin_user: str | unicode
        :param default_user: Specifies the default username for which a credential will be generated.
        :type default_user: str | unicode
        :param cidr_list: Specifies a comma separated list of CIDR blocks for which the role is applicable for.
        :type cidr_list: str | unicode
        :param exclude_cidr_list: Specifies a comma-separated list of CIDR blocks.
        :type exclude_cidr_list: str | unicode
        :param port: Specifies the port number for SSH connection.
        :type port: int
        :param key_type:  Specifies the type of credentials generated by this role.
        :type key_type: str | unicode
        :param key_bits: Specifies the length of the RSA dynamic key in bits. (default: 1024)
        :type key_bits: int
        :param install_script: Specifies the script used to install and uninstall public keys in the target machine.
        :type install_script: str | unicode
        :param allowed_users: If only certain usernames are to be allowed, then this list enforces it.
        :type allowed_users: str | unicode
        :param allowed_users_template: If set, allowed_users can be specified using identity template policies.
            (default: flase)
        :type allowed_users_template: bool
        :param allowed_domains: The list of domains for which a client can request a host certificate.
        :type allowed_domains: str | unicode
        :param key_option_specs: Specifies a comma separated option specification which will be prefixed to RSA keys in
            the remote host's authorized_keys file.
        :type key_option_specs: str | unicode
        :param ttl: Specifies the Time To Live value provided as a string duration with time suffix.
        :type ttl: string | unicode
        :param max_ttl: Specifies the Time To Live value provided as a string duration with time suffix.
        :type max_ttl: str | unicode
        :param allowed_critical_options: Specifies a comma-separated list of critical options that certificates can have
            when signed.
        :type allowed_critical_options: str | unicode
        :param allowed_extensions: Specifies a comma-separated list of extensions that certificates can have when
            signed.
        :type allowed_extensions: str | unicode
        :param default_critical_options: Specifies a map of critical options certificates should have if none are
            provided when signing.
        :type default_critical_options: dict
        :param default_extensions: Specifies a map of extensions certificates should have if none are provided when
            signing.
        :type default_extensions: dict
        :param allow_user_certificates: Specifies if certificates are allowed to be signed for use as a 'user'.
            (default: False)
        :type allow_user_certificates: bool
        :param allow_host_certificates: Specifies if certificates are allowed to be signed for use as a 'host'.
            (default: False)
        :type allow_host_certificates: bool
        :param allow_bare_domains: Specifies if host certificates that are requested are allowed to use the base domains
            listed in allowed_domains, e.g. "example.com". (default: False)
        :type allow_bare_domains: bool
        :param allow_subdomains: Specifies if host certificates that are requested are allowed to be subdomains of those
            listed in allowed_domains. (default: False)
        :type allow_subdomains: bool
        :param allow_user_key_ids: Specifies if users can override the key ID for a signed certificate with the "key_id"
            field. (default: False)
        :type allow_user_key_ids: bool
        :param key_id_format: When supplied, this value specifies a custom format for the key id of a signed
            certificate.
        :type key_id_format: str | unicode
        :param allowed_user_key_lengths: Specifies a map of ssh key types and their expected sizes which are allowed to
            be signed by the CA type.
        :type allowed_user_key_lengths: dict
        :param algorithm_signer: Algorithm to sign keys with. (default: "default")
        :type algorithm_signer: str | unicode
        :param mount_point: Specifies the place where the secrets engine will be accessible (default: ssh).
        :type mount_point: str | unicode
        :return: The JSON response of the request
        :rtype: aiohttp.ClientResponse
        """
        params = {
            "key": key,
            "admin_user": admin_user,
            "default_user": default_user,
            "cidr_list": cidr_list,
            "exclude_cidr_list": exclude_cidr_list,
            "port": port,
            "key_type": key_type,
            "key_bits": key_bits,
            "install_script": install_script,
            "allowed_users": allowed_users,
            "allowed_users_template": allowed_users_template,
            "allowed_domains": allowed_domains,
            "key_option_specs": key_option_specs,
            "ttl": ttl,
            "max_ttl": max_ttl,
            "allowed_critical_options": allowed_critical_options,
            "allowed_extensions": allowed_extensions,
            "default_critical_options": default_critical_options,
            "default_extensions": default_extensions,
            "allow_user_certificates": allow_user_certificates,
            "allow_host_certificates": allow_host_certificates,
            "allow_bare_domains": allow_bare_domains,
            "allow_subdomains": allow_subdomains,
            "allow_user_key_ids": allow_user_key_ids,
            "key_id_format": key_id_format,
            "allowed_user_key_lengths": allowed_user_key_lengths,
            "algorithm_signer": algorithm_signer,
        }

        api_path = utils.format_url(
            "/v1/{mount_point}/roles/{name}", mount_point=mount_point, name=name
        )

        return await self._adapter.post(url=api_path, json=params)

    async def read_role(
        self,
        name="",
        mount_point=DEFAULT_MOUNT_POINT,
    ):
        """This endpoint queries a named role.

        :param name: Specifies the name of the role to read.
        :type name: str | unicode
        :param mount_point: Specifies the place where the secrets engine will be accessible (default: ssh).
        :type mount_point: str | unicode
        :return: The JSON response of the request
        :rtype: aiohttp.ClientResponse
        """
        api_path = utils.format_url(
            "/v1/{mount_point}/roles/{name}",
            mount_point=mount_point,
            name=name,
        )

        return await self._adapter.get(url=api_path)

    async def list_roles(
        self,
        mount_point=DEFAULT_MOUNT_POINT,
    ):
        """This endpoint returns a list of available roles. Only the role names are returned, not any values.

        :param mount_point: Specifies the place where the secrets engine will be accessible (default: ssh).
        :type mount_point: str | unicode
        :return: The JSON response of the request
        :rtype: aiohttp.ClientResponse
        """
        api_path = utils.format_url("/v1/{mount_point}/roles", mount_point=mount_point)

        return await self._adapter.list(url=api_path)

    async def delete_role(self, name="", mount_point=DEFAULT_MOUNT_POINT):
        """This endpoint deletes a named role.

        :param name:
        :type name: str | unicode
        :param mount_point: Specifies the place where the secrets engine will be accessible (default: ssh).
        :type mount_point: str | unicode
        :return: The JSON response of the request
        :rtype: aiohttp.ClientResponse
        """
        api_path = utils.format_url(
            "/v1/{mount_point}/roles/{name}",
            mount_point=mount_point,
            name=name,
        )

        return await self._adapter.delete(url=api_path)

    async def list_zeroaddress_roles(
        self,
        mount_point=DEFAULT_MOUNT_POINT,
    ):
        """This endpoint returns the list of configured zero-address roles.

        :param mount_point: Specifies the place where the secrets engine will be accessible (default: ssh).
        :type mount_point: str | unicode
        :return: The JSON response of the request
        :rtype: aiohttp.ClientResponse
        """
        api_path = utils.format_url(
            "/v1/{mount_point}/config/zeroaddress",
            mount_point=mount_point,
        )

        return await self._adapter.get(url=api_path)

    async def configure_zeroaddress_roles(
        self,
        roles="",
        mount_point=DEFAULT_MOUNT_POINT,
    ):
        """This endpoint configures zero-address roles.

        :param roles: Specifies a string containing comma separated list of role names which allows credentials to be requested for any IP address.
        :type roles: str | unicode
        :param mount_point: Specifies the place where the secrets engine will be accessible (default: ssh).
        :type mount_point: str | unicode
        :return: The JSON response of the request
        :rtype: aiohttp.ClientResponse
        """
        params = {
            "roles": roles,
        }

        api_path = utils.format_url(
            "/v1/{mount_point}/config/zeroaddress",
            mount_point=mount_point,
        )

        return await self._adapter.post(
            url=api_path,
            json=params,
        )

    async def delete_zeroaddress_role(self, mount_point=DEFAULT_MOUNT_POINT):
        """This endpoint deletes the zero-address roles configuration.

        :param mount_point: Specifies the place where the secrets engine will be accessible (default: ssh).
        :type mount_point: str | unicode
        :return: The JSON response of the request
        :rtype: aiohttp.ClientResponse
        """
        api_path = utils.format_url(
            "/v1/{mount_point}/config/zeroaddress", mount_point=mount_point
        )

        return await self._adapter.delete(
            url=api_path,
        )

    async def generate_ssh_credentials(
        self,
        name="",
        username="",
        ip="",
        mount_point=DEFAULT_MOUNT_POINT,
    ):
        """This endpoint creates credentials for a specific username and IP with the parameters defined in the given role.

        :param name: Specifies the name of the role to create credentials against. This is part of the request URL.
        :type name: str | unicode
        :param username: Specifies the username on the remote host.
        :type username: str | unicode
        :param ip: Specifies the IP of the remote host.
        :type ip: str | unicode
        :param mount_point: Specifies the place where the secrets engine will be accessible (default: ssh).
        :type mount_point: str | unicode
        :return: The JSON response of the request
        :rtype: aiohttp.ClientResponse
        """
        params = {
            "username": username,
            "ip": ip,
        }

        api_path = utils.format_url(
            "/v1/{mount_point}/creds/{name}",
            mount_point=mount_point,
            name=name,
        )

        return await self._adapter.post(url=api_path, json=params)

    async def list_roles_by_ip(
        self,
        ip="",
        mount_point=DEFAULT_MOUNT_POINT,
    ):
        """This endpoint lists all of the roles with which the given IP is associated.

        :param ip: Specifies the IP of the remote host.
        :type ip: str | unicode
        :param mount_point: Specifies the place where the secrets engine will be accessible (default: ssh).
        :type mount_point: str | unicode
        :return: The JSON response of the request
        :rtype: aiohttp.ClientResponse
        """
        params = {
            "ip": ip,
        }

        api_path = utils.format_url(
            "/v1/{mount_point}/lookup",
            mount_point=mount_point,
        )

        return await self._adapter.post(
            url=api_path,
            json=params,
        )

    async def verify_ssh_otp(
        self,
        otp,
        mount_point=DEFAULT_MOUNT_POINT,
    ):
        """This endpoint verifies if the given OTP is valid. This is an unauthenticated endpoint.

        :param otp: Specifies the One-Time-Key that needs to be validated.
        :type otp: str | unicode
        :param mount_point: Specifies the place where the secrets engine will be accessible (default: ssh).
        :type mount_point: str | unicode
        :return: The JSON response of the request
        :rtype: aiohttp.ClientResponse
        """
        params = {
            "otp": otp,
        }

        api_path = utils.format_url(
            "v1/{mount_point}/verify",
            mount_point=mount_point,
        )

        return await self._adapter.post(
            url=api_path,
            json=params,
        )

    async def submit_ca_information(
        self,
        private_key="",
        public_key="",
        generate_signing_key=True,
        key_type="ssh-rsa",
        key_bits=0,
        mount_point=DEFAULT_MOUNT_POINT,
    ):
        """This endpoint allows submitting the CA information for the secrets engine via an SSH key pair.

        :param private_key: Specifies the private key part the SSH CA key pair.
        :type private_key: str | unicode
        :param public_key: Specifies the public key part of the SSH CA key pair.
        :type public_key: str | unicode
        :param generate_signing_key: Specifies if Vault should generate the signing key pair internally. (default: True)
        :type generate_signing_key: bool
        :param key_type: Specifies the desired key type for the generated SSH CA key when generate_signing_key is set to true. (default: ssh-rsa)
        :type key_type: str | unicode
        :param key_bits: Specifies the desired key bits for the generated SSH CA key when generate_signing_key is set to true. (default: 0)
        :type key_bits: int
        :param mount_point: Specifies the place where the secrets engine will be accessible (default: ssh).
        :type mount_point: str | unicode
        :return: The JSON response of the request
        :rtype: aiohttp.ClientResponse
        """
        params = {
            "private_key": private_key,
            "public_key": public_key,
            "generate_signing_key": generate_signing_key,
            "key_type": key_type,
            "key_bits": key_bits,
        }

        api_path = utils.format_url(
            "/v1/{mount_point}/config/ca",
            mount_point=mount_point,
        )

        return await self._adapter.post(
            url=api_path,
            json=params,
        )

    async def delete_ca_information(
        self,
        mount_point=DEFAULT_MOUNT_POINT,
    ):
        """This endpoint deletes the CA information for the backend via an SSH key pair.

        :param mount_point: Specifies the place where the secrets engine will be accessible (default: ssh).
        :type mount_point: str | unicode
        :return: The JSON response of the request
        :rtype: aiohttp.ClientResponse
        """
        api_path = utils.format_url(
            "/v1/{mount_point}/config/ca",
            mount_point=mount_point,
        )

        return await self._adapter.delete(url=api_path)

    async def read_public_key(
        self,
        mount_point=DEFAULT_MOUNT_POINT,
    ):
        """This endpoint reads the configured/generated public key.

        :param mount_point: Specifies the place where the secrets engine will be accessible (default: ssh).
        :type mount_point: str | unicode
        :return: The JSON response of the request
        :rtype: aiohttp.ClientResponse
        """
        # TODO Consider if the unauthenticated endpoint could be used if not authenticated
        api_path = utils.format_url(
            "/v1/{mount_point}/config/ca",
            mount_point=mount_point,
        )

        return await self._adapter.get(url=api_path)

    async def sign_ssh_key(
        self,
        name="",
        public_key="",
        ttl="",
        valid_principals="",
        cert_type="user",
        key_id="",
        critical_options=None,
        extensions=None,
        mount_point=DEFAULT_MOUNT_POINT,
    ):
        """This endpoint signs an SSH public key based on the supplied parameters,
        subject to the restrictions contained in the role named in the endpoint.

        :param name: Specifies the name of the role to sign. This is part of the request URL.
        :type name: str | unicode
        :param public_key: Specifies the SSH public key that should be signed.
        :type public_key: str | unicode
        :param ttl: Specifies the Requested Time To Live.
        :type ttl: str | unicode
        :param valid_principals: Specifies valid principals that the certificate should be signed for.
        :type valid_principals: str | unicode
        :param cert_type: Specifies the type of certificate to be created; either "user" or "host". (default: user)
        :type cert_type: str | unicode
        :param key_id: Specifies the key id that the created certificate should have.
        :type key_id: str | unicode
        :param critical_options: Specifies a map of the critical options that the certificate should be signed for.
        :type critical_options: dict
        :param extensions: Specifies a map of the extensions that the certificate should be signed for.
        :type extensions: dict
        :param mount_point: Specifies the place where the secrets engine will be accessible (default: ssh).
        :type mount_point: str | unicode
        :return: The JSON response of the request
        :rtype: aiohttp.ClientResponse
        """
        params = {
            "public_key": public_key,
            "ttl": ttl,
            "valid_principals": valid_principals,
            "cert_type": cert_type,
            "key_id": key_id,
            "critical_options": critical_options,
            "extensions": extensions,
        }

        api_path = utils.format_url(
            "/v1/{mount_point}/sign/{name}", mount_point=mount_point, name=name
        )

        return await self._adapter.post(
            url=api_path,
            json=params,
        )
