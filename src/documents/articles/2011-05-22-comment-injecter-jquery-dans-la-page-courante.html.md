---
layout: post
date: "2011-05-22 21:56:32"
title: "Comment injecter jQuery dans la page courante ?"
tags:
 - bookmarklet
 - jquery

---

Je suis en pleine découverte de Node.JS, MongoDB et tout. Je manipule forcément du Javascript, et dans certains cas il manque les fonctionnalités de son framework préféré pour utiliser un service REST par exemple.

Voici une petite astuce, permettant d'injecter un fichier JS dans le DOM de la page.

```javascript
javascript:void((function(){
    var s=document.createElement('script');
    s.setAttribute('src','http://ajax.googleapis.com/ajax/libs/jquery/1.6.1/jquery.js');
    document.body.appendChild(s);
    void(s);
})())
```

Il suffit de déplacer ce lien dans votre barre des signets, de ce fait lorsque vous cliquerez dessus le code JS sera executé, et injectera dans mon cas jQuery.
