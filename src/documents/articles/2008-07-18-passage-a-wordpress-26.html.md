---
layout: post
date: 2008-07-18 13:16:38
title: "Passage à Wordpress 2.6"
tags:
 - g33k
 - mise a jour
 - pathinfo
 - rewriting
 - url
 - wordpress

---

Une mise à jour plutôt sous le signe de la galère ... En général ça se passe sans pb ! Bien pas cette fois !

  * Problème de reconnaissance du préfixe de la base
  * Autorisations révoquées
  * Import partiel ...
  * Activation de l'URL Rewriting chez TuxFamily, donc toutes les pages en 404
  * Problèmes de référencements
  * Que du bonheur ...

Normalement tout est revenu à la normal.
Avec un redirect 301 pour corriger le problème de PATHINFO.
