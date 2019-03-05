import mongoengine


def global_init():
    mongoengine.register_connection(alias='core', name='rss', host='mongodb+srv://felipe:a1b2c3d4e5@cluster0-twctd.mongodb.net/rss?retryWrites=true')

    #yvgYrHnph2DYiT35