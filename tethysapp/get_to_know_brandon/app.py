from tethys_sdk.base import TethysAppBase, url_map_maker


class GetToKnowBrandon(TethysAppBase):
    """
    Tethys app class for About Me.
    """

    name = 'About Me'
    index = 'get_to_know_brandon:home'
    icon = 'get_to_know_brandon/images/azflag.png'
    package = 'get_to_know_brandon'
    root_url = 'get-to-know-brandon'
    color = '#a51c1c'
    description = 'Get to know your friendly neighborhood web app developer'
    tags = 'info,aboutme,nerdalicious'
    enable_feedback = False
    feedback_emails = []

    def url_maps(self):
        """
        Add controllers
        """
        UrlMap = url_map_maker(self.root_url)

        url_maps = (
            UrlMap(
                name='home',
                url='get-to-know-brandon',
                controller='get_to_know_brandon.controllers.home'
            ),
            UrlMap(
                name='ilike',
                url='get-to-know-brandon/ilike',
                controller='get_to_know_brandon.controllers.ilike'
            ),
            UrlMap(
                name='imfrom',
                url='get-to-know-brandon/imfrom',
                controller='get_to_know_brandon.controllers.imfrom'
            ),
        )

        return url_maps
