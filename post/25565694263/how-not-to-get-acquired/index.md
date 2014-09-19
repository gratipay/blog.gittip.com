---
title: How Not to Get Acquired
dateline: June 21, 2012, 4:46 am
layout: page
---

<p>I launched <a href="https://www.gittip.com/">Gittip.com</a> 16 days ago. It
saw really strong initial uptake, then it got side-swiped by a botched
acquisition. Herewith, a cautionary tale.</p><hr>

<p><strong>Update:</strong> I had a phone conversation with Sean Harper, co-
founder of FeeFighters, which is <a
href="http://news.ycombinator.com/item?id=4143798">summarized in this Hacker
News comment</a>.</p>

<p><strong>Update 2:</strong> Here is <a
href="http://news.ycombinator.com/item?id=4144075">a general response from
Sean</a>.</p><hr><h4>My Beginnings with Samurai</h4>

<p>I don&#8217;t remember where I first ran across <a
href="https://samurai.feefighters.com/">Samurai</a> exactly. It is (was) a
credit-card processing product from a start-up called FeeFighters. I was drawn
in by their well-designed marketing site, which carried through into the
management UI and the API. Good first impression. There were one or two rough
edges signing up for their service, but all in all it was smooth. And what
hiccups there were were more than compensated for by their excellent customer
service. Multiple team members were available in a Campfire chatroom, at all
hours. I ended up getting acquainted with two in particular, <a
href="https://twitter.com/#!/seanharper">Sean Harper</a>, the CEO, and <a
href="https://twitter.com/#!/pitdesi">Sheel Mohnot</a>, in charge of business
development. I live in Pittsburgh, where Sheel went to school, and they&#8217;re
in Chicago, where I went to school, so we connected easily.</p>

<p>My first project using Samurai was the Minimum Viable App. Literally all it
did was allow people to give me money via credit card. I made my first online
dollar through the site. My second project was <a
href="https://www.ihasamoney.com/">IHasAMoney.com</a>, a personal finance
website for geeks&#8212;Mint.com sans the evil; $2.99 a month. As of this
writing that site is still up, though it&#8217;s stalled because there really is
no good way to aggregate financial data apart from what Mint does, namely, <a
href="http://www.youtube.com/watch?v=H841U6RhrDU#t=5m39s">storing cleartext
passwords and screenscraping your bank</a>:</p>

<p><iframe frameborder="0" height="360"
src="http://www.youtube.com/embed/H841U6RhrDU#t=5m39s" width="480"></iframe></p>

<p>Plan C (more like plan N, really): Gittip! Tips for GitHub, but so much more.
Recurring micro-payment gifts, <a href="https://www.gittip.com/about/">crowd-
sourced genius grants for the rest of us</a>. Sweet, okay. Samurai! Well, it
turns out that in the seven months since I became a customer, FeeFighters was <a
href="http://techcrunch.com/2012/03/23/groupon-acquires-feefighters-the-
billshrink-for-business-services/">acquired by GroupOn</a>. The <a
href="http://feefighters.com/blog/feefighters-acquired/">horse says</a>,
predictably, that &#8220;[t]he FeeFighters marketplace, our Samurai gateway and
the FeeFighters and Samurai brands are continuing as before.&#8221; Hacker News
is <a href="http://news.ycombinator.com/item?id=3747076">doubtful</a>.</p>

<p>Unfortunately, the doubters were right, in my experience.</p><h4>Samurai Fails Me When I Need It Most</h4>

<p>Gittip operates on a weekly schedule. We pull money in via credit card every
Friday and distribute gifts averaging about 50¢ amongst the members of the
Gittip community. In week one we moved $25. In week two we were supposed to move
$55, more than double the first week. But Samurai failed. Over half of the
credit cards we attempted to bill failed with the message: &#8220;undefined
method `[]&#8217; for false:FalseClass,&#8221; which smells to me a lot more
like a Samurai issue than a genuine credit card failure. We moved $4.</p>

<p>So I reached out. Naturally, I went first to the Campfire chatroom where I
had first gotten to know Sean and the team. Turns out it&#8217;s now <a
href="http://feefighters.campfirenow.com/db381">password-protected</a>. Okay,
let&#8217;s try the phone number, +1-855-FIGHTER (344-4837). Go ahead and call
it. See if you get a recording, &#8220;You have reached a non-working
number,&#8221; like I do. This was the point at which I discovered via Google
that they had been acquired.</p>

<p>I started looking at other vendors. I&#8217;d heard good things about both <a
href="https://stripe.com/">Stripe</a> and <a
href="https://www.braintreepayments.com/">Braintree</a>, and quickly ended up in
conversations with both. My Braintree sales rep (also in Chicago) offered that
GroupOn had let the FeeFighters support team go, and had only kept Sean and one
dev. That&#8217;s from a competitor, and I&#8217;d take it with a grain of salt,
except that all the support channels have, in fact, been shut down. It turns out
that I sent three emails to samurai@feefighters.com, which <a
href="https://feefighters.zendesk.com/home">funnels into a ZenDesk</a>, starting
on May 15. The first one ends with, &#8220;P.S. No more campfire?&#8221; All are
status &#8220;new&#8221; and unassigned.</p>

<p><img src="http://media.tumblr.com/tumblr_m5yh2ovn5Y1rn81gb.png"/></p>

<p>I reached out on Twitter. I tweeted @FeeFighters five times (<a
href="https://twitter.com/whit537/status/213002729352740864">1</a>, <a
href="https://twitter.com/whit537/status/213656702732599296">2</a>, <a
href="https://twitter.com/whit537/status/213656968949284864">3</a>, <a
href="https://twitter.com/whit537/status/213721111668592640">4</a>, <a
href="https://twitter.com/whit537/status/215447889437147136">5</a>). No response
yet. I <a href="https://twitter.com/whit537/status/215233861012041728">asked
Sean</a> to help me migrate my data. No response yet. I <a
href="https://twitter.com/whit537/status/215447889437147136">invited Sheel</a>
to shed some light. No response yet. I emailed Sheel per <a
href="http://news.ycombinator.com/user?id=pitdesi">his Hacker News profile</a>.
No response yet.</p>

<p>In the mean time, of course, my first remotely successful venture in 10 years
of trying is in danger of getting squished right out of the gate. More
importantly, I&#8217;m on the hook for 25 people&#8217;s credit card data stored
PCI-compliantly away inside a dying system. Gah!</p>

<p>So I <a href="https://github.com/whit537/www.gittip.com/issues/58">migrated
to Stripe</a>. I still may implement Braintree as a back-up, but there I&#8217;m
blocked on trying to migrate my merchant account over from Samurai. Stripe
doesn&#8217;t even give me the option of bringing my own merchant account. I
also learned about <a href="https://www.dwolla.com/">Dwolla</a> in all of this,
and I&#8217;m really <a
href="https://github.com/whit537/www.gittip.com/issues/65">interested</a> in
it. But Stripe was the lowest-hanging fruit.</p><h4>Bottom Line for Gittip Users</h4>

<p>Unfortunately, I felt that I had to redact all of the credit card
information that I had stored with Samurai on behalf of Gittip&#8217;s users. I
certainly didn&#8217;t feel comfortable leaving your data inside a dying system,
and without support from FeeFighters, now GroupOn, I couldn&#8217;t migrate that
data out. This means that Gittip is currently down to one credit card on file,
mine, and I&#8217;m here trying to salvage the momentum of the first two weeks,
during which Gittip had 5,900 unique visitors, 515 sign-ups, 25 credit cards
entered, and some <a
href="https://github.com/whit537/www.gittip.com/issues/28">amazing community
involvement</a>.</p>

<p>That said, I should have taken it more seriously when on May 15 I started
noticing that FeeFighters was missing in action. I&#8217;m sorry for ignoring
the warning signs and entrusting your data to a struggling vendor. If you still
believe in Gittip and would like to help it bounce back, you can <a
href="https://www.gittip.com/credit-card.html">re-enter your credit card details
here</a>.</p>
