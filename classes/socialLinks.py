import webbrowser as link

class SocialLinks():
    def __ini__(self):
        pass

    def openLink(self, site):
        self.site = site

        if self.site == 'discord':
            url = 'https://discord.com/channels/@me/961905056578416660'
        elif self.site == 'twitter':
            url = 'https://twitter.com/_katiorro'
        elif self.site == 'github':
            url = 'https://github.com/pySiriusDev?tab=repositories'
        elif self.site == 'paypal':
            url = 'https://www.paypal.com/donate/?hosted_button_id=X74DV8VCZH84A'

        link.open(url)
