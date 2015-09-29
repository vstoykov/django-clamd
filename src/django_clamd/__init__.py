

def get_scanner():
    """Lazy get scanner configured scanner when needed"""
    import clamd
    from . import conf

    if conf.CLAMD_USE_TCP:
        return clamd.ClamdNetworkSocket(conf.CLAMD_TCP_ADDR, conf.CLAMD_TCP_SOCKET)

    return clamd.ClamdUnixSocket(conf.CLAMD_SOCKET)
