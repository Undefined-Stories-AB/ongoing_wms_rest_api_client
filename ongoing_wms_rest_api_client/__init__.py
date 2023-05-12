""" A client library for accessing Ongoing WMS Goods Owner REST API """
from .client import AuthenticatedClient, Client

__all__ = (
    "AuthenticatedClient",
    "Client",
)
