from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack

import task_list.routing


application = ProtocolTypeRouter({
    'websocket': AuthMiddlewareStack(
        URLRouter(task_list.routing.websocket_urlpatterns)
    ),
})
