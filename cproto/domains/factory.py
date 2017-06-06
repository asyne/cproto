class BaseDomain(object):
    pass


def get_command(domain_name, command_name):
    """Returns a closure function that dispatches message to the WebSocket."""
    def send_command(self, **kwargs):
        return self.ws.send_message(
            '{0}.{1}'.format(domain_name, command_name),
            kwargs
        )

    return send_command


def DomainFactory(domain_name, cmds):
    """Dynamically create Domain class and set it's methods."""
    klass = type(str(domain_name), (BaseDomain,), {})

    for c in cmds:
        command = get_command(domain_name, c['name'])
        setattr(klass, c['name'], classmethod(command))

    return klass
