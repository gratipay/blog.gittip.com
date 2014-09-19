---
title: Stolen Money on Gittip, Part 1
dateline: November 5, 2012, 10:04 am
layout: page
---

<p><a href="https://www.gittip.com/">Gittip</a> is a platform for sustainable
crowd-funding. It allows you to set up small weekly gifts between $1 and $24 to
people you believe in. Gittip is about five months old, and currently has about
550 active users, with $1,400 changing hands per week.</p>

<p>On October 10 (27 days ago), I <a
href="https://twitter.com/whit537/status/256125103643963392">noticed</a> a new
user named <a href="https://www.gittip.com/delpan/">delpan</a> in the top ten
receivers list on the Gittip homepage. This user was suspicious, because the
associated GitHub account was recently created, and empty: no repos; no
followers, starred, or following; no name or location or avatar. Gittip has
grown by word of mouth, so to have a new user unconnected to the rest of the
Gittip social graph is unusual. But I didn&#8217;t want to jump to conclusions.
There&#8217;s a Counter-Strike player that goes by delpan; maybe Gittip was
breaking out into a new community? We <a
href="https://github.com/whit537/www.gittip.com/issues/329">adopted</a> a wait
and see approach.</p>

<p>Since then, it has become clear that delpan and other accounts on Gittip are
in fact being used to steal money. The basic pattern is to create two Gittip
accounts, one linked to a stolen credit card, the other to a bank account, with
a tip set up from the one to the other. On payday, Gittip pulls the money in
from the credit card and deposits it in the bank account. It does this via <a
href="https://www.balancedpayments.com/">Balanced</a>, Gittip&#8217;s payment
processing <a href="http://blog.gittip.com/post/28351995405/open-
partnerships">partner</a>.</p>

<p>I have identified six Gittip accounts that I strongly believe are linked to
stolen credit cards. I determined this by manually reviewing the top 100 or so
givers on Gittip, and looking for patterns. My heuristic boiled down to the
following:</p>

<ul>

<li>The Gittip account is associated with an empty or suspended Twitter or
GitHub account.</li>

<li>Tips include significant tips to other Gittip accounts with empty or
suspended Twitter or GitHub accounts.</li></ul>

<p>Secondary factors included:</p>

<ul>

<li>The Gittip account is anonymous on the giver&#8217;s leaderboard.</li>

<li>The &#8220;I am making the world better by &#8230;&#8221; statement is
vacuous.</li>

<li>The username is CamelCased.</li></ul>

<p>I have reported these six accounts to Balanced. Together, these
accounts have been used to steal $488.15 since September 27. The total charge
volume during this six week period was $8,414.92, so the money stolen through
these six accounts comprises 6% of Gittip&#8217;s volume during that time.
However, we had <a
href="https://twitter.com/whit537/status/258939505388707841">an unusual
number</a> of credit card failures during the October 18 payday, and unless new
stolen cards were associated with the same Gittip account, which I only noticed
in one of the six cases, these would not have been reflected in the top 100 at
the time I conducted the review. Consequently, I expect that even more stolen
money has been funneled through Gittip. I need to do more research to determine
how much.</p>

<p>Where is the stolen money now? Again, I need to do more research to fully
answer the question. Anecdotally, most has gone to suspicious Gittip accounts,
though a significant portion has also gone to legitimate Gittip users. Some
remains escrowed within Gittip, some has been regifted, some withdrawn to a bank
account&#8212;again, both by suspicious and legitimate Gittip users. Some has
been paid to Gittip and Balanced as fees. The ideal is to get the money back to
the people it was stolen from. Is this feasible? Do Visa and Mastercard make
this possible?</p>

<p>The uncomfortable truth is that Gittip, Balanced, and our legitimate users
are financially incentivized to turn a blind eye to fraud, because we have
benefitted and are benefitting from it. I have stolen money in my bank account.
Heck, I pretty much have stolen money in my pocket right now. The difficulty of
unravelling the flow of money once it&#8217;s in the system makes this even less
comfortable. We&#8217;re accidentally complicit in the crime, with no easy way
to make good.</p><h4>What do we do?</h4>

<p>The most important thing is to prevent stolen money from entering the system
in the first place. Therefore, I am <a
href="https://github.com/whit537/www.gittip.com/issues/356">instituting a
whitelist</a>: every giver will be reviewed and approved before Gittip charges
their credit card. Gittip has about 350 credit cards on file and is only adding
a few each week right now, so for the immediate future I will just manually
review all paying accounts before payday each Thursday. I&#8217;ve already
started adding admin UI to facilitate this and updating the payday script to
enforce it, and no money was charged last week to the six accounts I
identified.</p>

<p>As Gittip scales, we&#8217;ll need to rely more on algorithms and less on
human intervention, though it&#8217;d be nice to avoid the <a
href="https://www.google.com/search?q=paypal%20nightmare">nightmare
scenarios</a> that people run into with PayPal. The fact that Gittip accounts
must be linked to a Twitter or GitHub account comes in handy here, and an
automated or semi-automated approach based on the heuristic above seems like a
good next step.</p>

<p>We still have the problem of recovering stolen money once it has entered the
system. I need to do more research to understand what that looks like and what
our options are with Balanced before I know how to proceed there, and
that&#8217;s why this is Part 1. Stay tuned &#8230;</p>

<p><strong>UPDATE:</strong> Here&#8217;s part two: <a
href="http://blog.gittip.com/post/35314128322/the-delpan-incident">The Delpan
Incident</a>.</p><hr>

<p><em><a href="https://www.gittip.com/whit537/">Chad Whitacre</a> is the
founder of Gittip.</em></p>
