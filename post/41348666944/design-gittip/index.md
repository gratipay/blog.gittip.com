---
title: Design Gittip
dateline: January 24, 2013, 3:08 am
layout: page
---

<p><span>Design community, I need your help. There’s a stigma associated with
</span><a href="https://www.gittip.com/">Gittip</a><span> that it’s only for
open source programmers. To be sure, some of that comes from the name (which we
</span><a href="https://github.com/zetaweb/www.gittip.com/issues/138">tried
hard</a><span> to change, but which we just need to live with for now). My sense
is that the bigger problem is that the visual design that Gittip launched with
seven months ago is holding us back from being taken seriously by the design
community and by design-conscious communities such as musicians, writers, and
artists. This is a bummer because that’s exactly who we want Gittip to work
for. I want to support my favorite musicians on Gittip.</span></p>

<p>Within weeks of launching we started a <a
href="https://github.com/zetaweb/www.gittip.com/issues/66">ticket</a> to
“change the visual design of Gittip.” It proved to be a fairly popular
ticket, and a month later we received a design contribution from <a
href="https://twitter.com/damon_sf">Damon Chin</a> (an employee of Gittip’s
payments partner, Balanced). This languished for want of an implementor until
last week, when <a href="http://nicksergeant.com/">Nick Sergeant</a> stepped
forward to convert Damon’s design to markup. That’s definitely going to move
the needle for us, and I’m grateful to Damon and Nick for diving in. This post
is about how to go even further.</p>

<p>Three weeks ago I announced that <a
href="http://blog.gittip.com/post/39687487576/gittip-is-hiring">Gittip is
hiring</a>. This caused some controversy due to the fact that, as an open
company, Gittip doesn’t compensate its employees, but the fact is that we now
have a dozen people actively contributing to Gittip. This is fantastic! Our
bottleneck, though, is front-end expertise.</p>

<p>Nick’s sweet spot for us is going to be converting design files to markup.
Damon’s contribution came through his employer, and, while I <a
href="http://whit537.org/2012/12/why-i-love-balanced.html">love</a> Balanced, we
need to not lean too heavily on them. Gittip needs to build its own team.
Therefore, I’m looking for <strong>someone with a passion for web product
design to join the Gittip team.</strong></p>

<p>What is it we’re building?</p><h4>Core Product</h4>

<p>Here’s a high-level overview of Gittip as a product:</p>

<ul>

<li><strong>Profiles. </strong>We enable individuals to tell a story about
how they’re making the world better.</li>

<li><strong>Giving.</strong> We enable individuals to participate in each
other’s stories through long-term, no-strings-attached, financial gifts.</li>

<li><strong>Communities.</strong> We enable communities to tell and sustain a
collective story.</li></ul><h4>Extension Points</h4>

<p>Here are the ways Gittip interfaces with other sites:</p>

<ul>

<li><strong>Connecting Accounts.</strong> We support connecting as many
other services as possible to a Gittip profile. A few of these other services
can also be used to authenticate with Gittip and/or move money into or out of
Gittip.</li>

<li><strong>Partnerships.</strong> We seek out partnerships with third parties
to add Gittip links in their products. We practice engineering as
marketing.</li>

<li><strong>Browser Extension.</strong> We provide extensions for all major
browsers, adding Gittip links on websites with whom we’re not yet
partners.</li>

<li><strong>Widgets.</strong> We provide ways for participants to embed Gittip
functionality on other websites.</li>

<li><strong>API.</strong> We provide APIs that enable third parties to build
tools for participants to work with their data stored in Gittip.</li></ul>

<div><h4>Visual Design Requirements</h4>

<p>Here are the visual design requirements for Gittip as I see them:</p>

<ul>

<li><strong>Name:</strong> “Gittip” (not “GitTip”)</li>

<li><strong>Motto:</strong> “Inspiring Generosity”</li>

<li><strong>Logo:</strong> <img alt="image" src="http://media.tumblr.com/ac566e8
621589d231c794020c7b53123/tumblr_inline_mh4b7bbEsY1rn81gb.png"/> (“Heart
Coin”)</li>

<li><strong>Colors:</strong> <img alt="image" src="http://media.tumblr.com/2d95c
d6ee261fb7d72a98555b92049e7/tumblr_inline_mh4b84OI3O1rn81gb.png"/> (#614C3E) and
<img alt="image" src="http://media.tumblr.com/135ee65a2f36d361d08b311a561d5dff/t
umblr_inline_mh4b8fgua91rn81gb.png"/> (#2A8F79)</li>

<li><strong>Typography</strong> is open game, but web fonts only (no typography
via images).</li>

<li><strong>Responsive</strong> design.</li>

<li>We can use <strong>Bootstrap</strong> (or another framework) for laying out
the grid and handling responsiveness, but &#8230;</li>

<li>We need to have a <strong>fully customized</strong> look and feel, including
forms.</li>

<li>Products I admire greatly: <strong><a
href="https://stripe.com/">Stripe</a></strong>, <strong><a
href="https://www.airbnb.com/">Airbnb</a></strong>, <strong><a
href="https://gumroad.com/">Gumroad</a></strong>.</li></ul></div><h4>Information Architecture</h4>

<p>Below are the pages we have and need for Gittip.</p>

<ul>

<li><strong>/</strong> - Homepage focuses on high-level aggregate data.</li>

<li><strong>/about/</strong> - More charts and other info.</li>

<li><strong>/%participant_id/</strong> - Allows individuals and groups to tell
their story, connect accounts elsewhere, and manage their giving.</li>

<li><strong>/%participant_id/funds/</strong> - Allows users to manage
“funds.” Think mutual funds; see <a href="https://github.com/zetaweb/www.git
tip.com/issues/449#issuecomment-12440694">this ticket</a> for a
description.</li>

<li><strong>/communities/%community/</strong> - Aggregates information about
givers, receivers, and funds within a certain community. Community pages are
described in <a href="https://github.com/zetaweb/www.gittip.com/issues/496">this
ticket</a>.</li>

<li><strong>/on/twitter/</strong>, etc. - Represent accounts on other services
that haven’t been connected to a Gittip account (<a
href="https://www.gittip.com/on/twitter/BarackObama/">example</a>), or
<em>groups</em> of accounts on other services (<a
href="https://www.gittip.com/on/github/zetaweb/">example</a>).</li></ul>

<p>That’s what we are building, and I believe that Gittip has nothing but
open road in front of it. From our <a
href="https://www.gittip.com/about/charts.html">charts</a> you can see that we
experienced strong early growth, and then hit a rough patch while I transitioned
out of my full time job in order to focus on Gittip. Now, here in 2013, we are
building a team and are starting to grow again. Our goal is to grow two orders
of magnitude over the next 18 months, and to do that we need a strong product
designer on board.</p>

<p>Do you want to join us? You can get in touch with me, Chad Whitacre, as
whit537 on <a href="http://dribbble.com/whit537">Dribbble</a> and <a
href="https://twitter.com/whit537">Twitter</a>, by email at <a
href="mailto:chad@zetaweb.com">chad@zetaweb.com</a>, or by phone at
+1-412-925-4220. IRC is another great way to connect; we hang out in #gittip on
Freenode.</p>

<p>Thank you, and I look forward to hearing from you! :^)</p><hr>

<p><em><a href="https://www.gittip.com/whit537/">Chad Whitacre</a> is the
founder of <a href="https://www.gittip.com/">Gittip</a>.</em></p>
