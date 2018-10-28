---
title: "Https enabled"
date: 2018-10-28T16:47:08+01:00
draft: false
---

I've been working on enabling SSL for this website.
In order not to overuse my brain on a Sunday,
I followed the instructions of a [DigitalOcean post](https://www.digitalocean.com/community/tutorials/how-to-secure-nginx-with-let-s-encrypt-on-ubuntu-16-04)
(they are so useful, I highly recommend checking them out).

The post make you use [Let's encrypt](https://letsencrypt.org/) with [Certbot](https://certbot.eff.org/).
In a few commands,
all is ready.
It almost felt like knowing what SSL certificates were and how they worked was not needed.
A big applause to the community who created both of them.
Certbot directly modify your Nginx file so you just have to check that it's alright.

One thing I had overlook when first setting the site was the firewall `ufw`,
I first had to configure it to accept both HTTP and HTTPS to Nginx.
When I set HTTP redirection to HTTPS, the firewall was blocking HTTPS,
making the site unreachable (hopefully no critical system depend on it :) ).
Once I figured that, all went smoothly.

I'm looking at how to enable comments in a Hugo website
(that is static).
For the moment, I think I'll go with [Isso](https://posativ.org/isso/),
it's open-source, require no third-party and come 'battery-included'.
