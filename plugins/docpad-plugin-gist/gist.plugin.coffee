module.exports = (BasePlugin) ->

    class GistPlugin extends BasePlugin
        name: 'gist'
    
        getGist = (opts, next) ->
            {content} = opts
            opts.content = content.replace /gist:([a-z0-9]+)/, (whole, m1) ->
                return '<code data-gist-id="' + m1 + '"></code>'
            return next()

        renderDocument: (opts, next) ->
            {extension, file} = opts
            if file.type is 'document' and extension is 'html'
                getGist opts,next
            else
                return next()