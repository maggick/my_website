Title: About
Date: 2015-02-16 20:40

# About Me

I am a security consultant.

## Open Source

I am an Open Source enthusiast. I discover this world in September 2009. My
first GNU/Linux installation was an Ubuntu 10.04 Lucid Linx in June 2010. So on
I always have a GNU/Linux distribution installed on my computer or my servers.
Actually my servers run on Debian and my desktops run on Arch Linux.

## maggick

I used maggick as a pseudo. This was given to me by my colleagues at Bearstech
in summer 2012. I used it on irc on github and on some forums.

## Contact

You can contact me via [Twitter](http://twitter.com/matthieukeller)
or [GitHub](http://github.com/maggick).

# About This Website

This website is hosted at [maggick.github.com](http://maggick.github.com) and
is redirected to [www.matthieukeller.com](http://www.matthieukeller.com). The
website is composed of two part : the blog and the notes. You can see the
"Technically" part to see how I managed both of them.

## History

This is the fifth version of this website :

* The first version was an home made website. Entirely write in HTML, CSS and PHP. It was a great exercise
  to learn the base of web 3-tier architecture with a client, a server and a database.
* The second version was powered by Word Press. In fact this was a classic WP with a plug-in for
  multi-languages and some simple changes in the default pages style.
* The third was generated using Middleman, a static site generator in Ruby wich
  generate HTML pages from markdown files.
* The fourth was build in html using the `markdown` command.

## Reasons that killed old versions

* The First version was huggly and almost without content.
* With the Word Press version I always have to use the online interface to create or update articles and pages.
  Moreover the data were on the site database, meaning that as I do not save them, they were not backuped as
  my usual data.
* With this version, I write pages in [Markdown format](https://github.com/github/markup#readme)
  directly on my computer with my favorite text editor, commit them on GitHub and finally put them on the server.
  There is no more database (meaning no more commentary, see the [About Me section](/about/me/##contact) for contact).
  The site is entirely static.
* The fourth version was not far from this one but it was long to make a small
  correction on a page (a spell correction for instance). I had to re-build the
  entire website and it was not automatically done.

## Technically

### Blog

The blog part is build with [Pelican](http://blog.getpelican.com/) and each
commit are pushed to my
[blog repository](https://github.com/maggick/blog) and the build is pushed to my
[maggick.github.io](http://github.com/maggick/maggick.github.io) repository.

### Notes

For this notebook part I use the
[MDwiki](http://dynalon.github.io/mdwiki/#!index.md) CMS in order to directly
generate HTML pages from the markdown files. This build is done in javascript,
meaning the work is totally deported on the client side.  Moreover I use
[github pages](http://pages.github.com/) to host my website. This mean that
every push to my github repository will lead to a direct update of the website !