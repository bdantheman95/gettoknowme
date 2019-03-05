from tethys_sdk.base import TethysAppBase, url_map_maker


class GetToKnowBrandon(TethysAppBase):
    """
    Tethys app class for About Me.
    """

    name = 'About Me'
    index = 'get_to_know_brandon:home'
    icon = 'get_to_know_brandon/images/icon.gif'
    package = 'get_to_know_brandon'
    root_url = 'get-to-know-brandon'
    color = '#a51c1c'
    description = '&quot;Get to know your friendly neighborhood web app developer&quot;'
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
        )

        return url_maps
