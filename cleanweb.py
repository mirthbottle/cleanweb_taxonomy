import twitter
import pandas as pd

def auth_twitter():
    token = twitter.oauth2_dance('FSIkjJmsDyZbL8SSzkeyIe1EY',
                                 'frk8TSxEtNuHZc1giR7PIb6PvtxqYD72GOSkRF8PFgTnQC8ybX')
    t = twitter.Twitter(auth=twitter.OAuth2(bearer_token=token))
    return t

# reponse.keys()
#[u'next_cursor_str',
# u'previous_cursor',
# u'users',
# u'next_cursor',
# u'previous_cursor_str']
def get_cleanweb_members(t):
    response = t.lists.members(owner_screen_name="CleanWebBos",
                               owner_id=531535685, slug="cleanweb-companies",
                               count=300, include_entities=False, skip_status=True)
    users = pd.DataFrame(response['users'])
    users = users.drop_duplicates(subset='name')
    # i want the name, description, url, screen_name, (location)
    return users[['name', 'description', 'url', 'screen_name']]


