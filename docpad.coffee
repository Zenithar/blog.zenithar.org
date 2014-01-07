marked = require('marked');

# The DocPad Configuration File
# It is simply a CoffeeScript Object which is parsed by CSON
docpadConfig = {

  environments:
    w:
      ignoreCustomPatterns: /2005|2006|2007|2008|2009|2010|2011|2012|2013/

  # Plugins configurations
  plugins:
    ghpages:
      deployRemote: 'origin'
      deployBranch: 'master'
      environment: 'static'
    navlinks:
      collections:
        posts: -1
    tags:
      extension: '.html'
      injectDocumentHelper: (document) ->
        document.setMeta(
          layout: 'tag'
        )
    rss:
      collection: 'posts'
      url: '/rss.xml'

  # =================================
  # Template Data
  # These are variables that will be accessible via our templates
  # To access one of these within our templates, refer to the FAQ: https://github.com/bevry/docpad/wiki/FAQ

  templateData:

    # Specify some site properties
    site: 

      services:
        buttons: ['GooglePlusOne', 'FacebookLike', 'FacebookFollow', 'TwitterTweet', 'TwitterFollow', 'GithubFollow']
        facebookLikeButton:
          applicationId: '72679093514'
        facebookFollowButton:
          applicationId: '72679093514'
          username: 'zenithar'
        twitterTweetButton: 'zenithar'
        twitterFollowButton: 'zenithar'
        githubFollowButton: 'zenithar'

      # The production url of our website
      url: "http://blog.zenithar.org"

      # Here are some old site urls that you would like to redirect from
      oldUrls: []

      # The default title of our website
      title: "Zenithar'z Blog"

      # The website description (for SEO)
      description: """
        Ancien ingénieur sécurité passionné, acteur dans le monde du logiciel 'libre'. Je suis en veille technologique permanente car toujours à la recherche du 'meilleur tournevis'.
        """

      # The website keywords (for SEO) separated by commas
      keywords: """
        zenithar,toulouse,java,security,engineer
        """

      # The website author's name
      author: "Thibault Normand"

      # The website author's email
      email: "me@zenithar.org"

  # -----------------------------
    # Helper Functions
    getTagUrl: (tag) ->
      t = tag.toLowerCase().replace(/[^a-z0-9]/g, '-').replace(/-+/g, '-').replace(/^-|-$/g, '')
      "/tags/#{t}.html"

    extractSummary: (contentRendered) ->
      markedOptions = {
        pedantic: false,
        gfm: true,
        sanitize: false,
        highlight: null
      }
      marked.setOptions(markedOptions)
      splited = marked(contentRendered).split(/<h[123456]/)
      splited[0]

    # Get the prepared site/document title
    # Often we would like to specify particular formatting to our page's title
    # we can apply that formatting here
    getPreparedTitle: ->
      # if we have a document title, then we should use that and suffix the site's title onto it
      if @document.title
        "#{@document.title} | #{@site.title}"
      # if our document does not have it's own title, then we should just use the site's title
      else
        @site.title

    # Get the prepared site/document description
    getPreparedDescription: ->
      # if we have a document description, then we should use that, otherwise use the site's description
      @document.description or @site.description

    # Get the prepared site/document keywords
    getPreparedKeywords: ->
      # Merge the document keywords with the site keywords
      return @site.keywords.concat(@document.keywords or []).join(', ')

  # =================================
  # Collections
  # These are special collections that our website makes available to us

  collections:
    #pages: (database) ->
    # database.findAllLive({pageOrder: $exists: true}, [pageOrder:1,title:1])

    posts: (database) ->
      database.findAllLive({layout:$has:'post'}, [date:-1])

  # =================================
  # DocPad Events

  # Here we can define handlers for events that DocPad fires
  # You can find a full listing of events on the DocPad Wiki
  events:

    # Server Extend
    # Used to add our own custom routes to the server before the docpad routes are added
    serverExtend: (opts) ->
      # Extract the server from the options
      {server} = opts
      docpad = @docpad
}


# Export our DocPad Configuration
module.exports = docpadConfig


# Convert a string to a color
# @see http://stackoverflow.com/questions/3426404/create-a-hexadecimal-colour-based-on-a-string-with-jquery-javascript
String::toColor = () ->
  hash = 0
  colour = "#"

  for i in [0..this.length-1]
    hash = this.charCodeAt(i++) + ((hash << 5) - hash)
  for i in [0..2]
    colour += ("00" + ((hash >> i++ * 8) & 0xFF).toString(16)).slice(-2)

  return colour

Date::toColor = () ->
  colors = ["#1abc9c", "#16a085", "#2ecc71", "#27ae60", "#3498db", "#2980b9", "#9b59b6", "#8e44ad", "#f1c40f", "#f39c12", "#e67e22", "#d35400", "#e74c3c", "#c0392b", "#95a5a6", "#7f8c8d" ]
  colors[this.getDate() % 16]

Date::getMonthName = () ->
  months = [ "Janvier", "Février", "Mars", "Avril", "Mai", "Juin", "Juillet", "Août", "Septembre", "Octobre", "Novembre", "Décembre" ]
  months[this.getMonth()]
