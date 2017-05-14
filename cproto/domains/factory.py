import json


class BaseDomain(object):
    @classmethod
    def send(cls, req):
        cls.ws.send(json.dumps(req))
        return cls.ws.recv()


def get_command(domain_name, command_name):
    def send_command(cls, **kwargs):
        return cls.send({
            'id': 0,
            'method': '{0}.{1}'.format(domain_name, command_name),
            'params': kwargs,
        })

    return send_command

def DomainFactory(domain_name, cmds):
    klass = type(str(domain_name), (BaseDomain,), {})

    for c in cmds:
        command = get_command(domain_name, c['name'])
        setattr(klass, c['name'], classmethod(command))

    return klass
