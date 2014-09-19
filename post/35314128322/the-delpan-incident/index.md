---
title: The Delpan Incident
dateline: November 8, 2012, 9:47 pm
layout: page
---

<p><a href="https://www.gittip.com/">Gittip</a> is a platform for sustainable
crowd-funding. It allows you to set up small weekly gifts between $1 and $24 to
people you believe in. Gittip is about five months old, and currently has about
550 active users, with about $1,500 changing hands per week.</p>

<p>Last week, we determined that <a
href="http://blog.gittip.com/post/35057426257/stolen-money-on-gittip-
part-1">stolen credit cards were being used on Gittip</a>. We started
investigating further to understand the nature and extent of the fraud, and we
started taking steps to undo it and prevent future fraud. This is part two of
that post. I named this incident the <strong>Delpan Incident</strong> after the
account we first suspected of fraud, and you can find a <a
href="https://www.gittip.com/about/fraud/2012-11-05.html">detailed incident
report here</a>.</p>

<p>I conclude that $567.89 of stolen money was injected into Gittip over a
period of seven weeks, representing 6% of credit card charges by dollar volume,
and 5% by number of transactions. The impact of the fraud is apparent in the
following chart, where the weeks in question are shaded red (the Gittip gift
exchange takes place every Thursday).</p>

<p><img src="http://media.tumblr.com/tumblr_md6hnfES1O1rn81gb.png"/></p>

<p>I apologize for this fraud, especially to the original victims of the credit
card theft, and to the ten innocent bystanders on Gittip who were affected.
I&#8217;m sorry.</p>

<p>I have investigated the network of relationships stemming from the five
accounts identified as fraudulent last week (a sixth account turned out to be
legitimate). I have also reviewed all accounts that moved money into or out of
Gittip in the past, and specifically those that had credit card failures in the
past. With help from the fraud and risk officer at <a
href="https://www.balancedpayments.com/">Balanced</a> (our payments provider), I
looked at account activity on GitHub accounts that were linked to Gittip
accounts that also have a bank account attached. My thanks to the employees of
Balanced and GitHub who helped out, as well as those anti-fraud professionals
who reached out in confidence via email or publicly on Hacker News and GitHub to
offer their expertise and support.</p>

<p>We now have an <em>is_suspicious</em> field in the Gittip database, with
options “yes”, “no,” and “maybe” (technically, true, false, and
null). Accounts start in the “maybe” category. Only accounts where
<em>is_suspicious</em> is “no” are allowed to move money from a credit card
into Gittip, or from Gittip out to a bank account. Accounts in the “maybe”
category may exchange gifts within Gittip, but can’t move money between Gittip
and the outside world. Accounts in the “yes” category are not included in
Gittip’s weekly gift exchange at all, nor are they permitted to login.
Whenever an account first links a credit card or bank account, it goes into a
queue and is reviewed before being included in the weekly gift exchange.</p>

<p>As a result of this investigation, a total of 22 accounts have been marked
suspicious, out of 6,308 (0.3%). None of these introduced money into the system
last week, and, as shown on the above chart, the dollar volume returned to an
amount in keeping with Gittip’s normal growth during the past three months.
Therefore, I believe that we’ve identified all accounts that have fraudulently
participated in the Gittip economy to date, and I have whitelisted all other
accounts that have successfully moved money into or out of Gittip in the past.
There are currently 431 whitelisted accounts on Gittip (7%).</p>

<p>Here’s a summary of the new categories:</p>

<p><strong>Is suspicious?</strong></p>

<p><strong>Yes</strong> - 22 (0.3%) - <em>Can&#8217;t move money at all;
can&#8217;t do anything</em></p>

<p><strong>No</strong> - 431 (6.8%) - <em>Can move money; unrestricted</em></p>

<p><strong>Maybe</strong> - 5,855 (92.8%) - <em>Can move money, but only inside
Gittip</em></p>

<p>Total - 6,308</p><h4>Making Good</h4>

<p>I have refunded the $567.89 of stolen money that was injected into Gittip. I
have notified Balanced of the bank accounts linked to suspicious accounts that
were used to withdraw $379.80 (67%) of the stolen money, and I am waiting to
hear whether they are able to recover any of that money. $104.00 (18%) of the
stolen money was given to ten innocent bystanders on Gittip, and will be
recovered from those individuals’ existing balances and future gifts. $54.00
(10%) is still escrowed within Gittip, and another $30.09 (5%) went to fees for
Balanced and Gittip, whence it will be recovered.</p>

<p>Then, there will be chargebacks. Victims of credit card theft have 120 days
to file a “chargeback” for each fraudulent charge, which then takes a month
or two to hit the affected merchant, Gittip in this case. Ideally, we’ve
identified all of the fraud on Gittip to date, and all stolen money has already
been refunded. However, a $15.00 fee applies for each fraudulent transaction
that we didn’t refund in time, before the chargeback process began.
(Chargebacks remove the moral burden of being complicit in fraud that I
expressed concern about in my <a href="http://blog.gittip.com/post/35057426257
/stolen-money-on-gittip-part-1">prior post</a>.)</p>

<p>I count 29 fraudulent transactions between 2 and 9 weeks ago, so in a worst
case scenario Gittip is looking at an additional $435.00 in fees. Assuming in
this scenario that the money already withdrawn to bank accounts is
unrecoverable, Gittip is looking at a burden of $814.80 for this incident, or
about 400% of the approximately $200.00 that Gittip has earned since launching.
Ultimately, whatever this burden turns out to be is the responsibility of Zeta
Design &amp; Development, LLC, the legal entity behind Gittip, and its owners,
namely, me.</p><h4>Lessons Learned</h4>

<p>It turns out that Gittip is particularly suited to a certain step in the <a
href="http://davepeck.org/2011/11/17/fraudsters-gonna-fraud/">black market for
stolen credit card numbers</a>, where low-level agents purchase long lists of
numbers and then verify which numbers are actually good by performing small
transactions with them. This is often done in the form of small donations to
charities that have simple, unsecured, online donation forms. However, the money
is lost from the point of view of the fraudster. With Gittip, it is possible to
set up a bank account on the other end to recover some of that waste. The upshot
is that Gittip is potentially useful for a certain kind of fraud, even though
Gittip doesn’t lend itself to quickly unloading large amounts of money from
any given card.</p>

<p>Fraud was bound to happen on Gittip sooner or later. Now we know one form it
will take. While the amount of bad money injected into Gittip was small this
time around—only $567.89—I much prefer to gain experience containing fraud
while the stakes are comparatively low than to have been overwhelmed by an even
greater degree of fraud now, or to learn an even harder lesson further down the
road. Gittip is better prepared for next time, with systems in place that we
didn’t have two weeks ago:</p>

<ul>

<li>A whitelisting policy for transactions with the outside world</li>

<li>The ability to blacklist fraudulent accounts entirely</li>

<li>A fraud dashboard and incident reporting infrastructure</li>

<li>Experience in data mining for fraud detection</li>

<li>A start on communicating additional fraud detection signals to Balanced</li>

<li>Relationships with anti-fraud professionals at partner companies and in the
broader tech industry</li></ul>

<p>Morever, this incident has given us a chance to test the principle of
“maximizing transparency” that is at the heart of what it means for Gittip
to be an <a href="http://blog.gittip.com/post/26350459746/the-first-open-
company">open company</a>. Rule #0 of anti-fraud is that you never tip your hand
in the arms race with fraudsters. Obfuscation and so-called “information
asymmetry” are the name of the game. What is the information that is
obfuscated? Fraud signals, machine learning algorithms that mine as much data as
you can get your hands on to find slight perturbations in the corporate
cognitive field, slight disturbances that warn of fraud. It&#8217;s considered a
truism that publicizing these algorithms gives fraudsters a much easier time
inventing new work-arounds.</p>

<p>I accept the starting-point that fraud will always exist. The task is not to
extirpate fraud—that’s impossible. Rather, it’s to keep it to a low enough
level for normal life to proceed apace. It’s like insanity. Each of us has a
tinge of insanity, but as long as we’re 99.5% normal, nobody notices. I also
grant that sociopaths walk among us. Heath Ledger’s Joker has been my mental
image during this episode. Why commit fraud? Wrong question. And yet, at this
point, my own question is, can I make my fraud algorithms public, and still keep
fraud below that 0.5% threshold? Because if I can, I want to. That said, I
respect the right of Balanced and Gittip’s other partners to manage fraud on
their own traditional, closed terms. There are fairly clear layers here between
Gittip and our partners, and I believe Gittip can experiment with openness
without jeopardizing the integrity of our partners’ anti-fraud efforts.</p>

<p>I don’t know exactly what this looks like yet, or whether I’ll end up
giving up and pursuing an information-asymmetric arms race per the status quo.
The <a href="https://www.gittip.com/about/fraud/2012-11-05.html">incident
report</a> I published is a first step in exploring how transparent Gittip can
be with regard to fraud. I hope to push that envelope further as Gittip grows.
Stay tuned &#8230;</p><hr>

<p><em><a href="https://www.gittip.com/whit537/">Chad Whitacre</a> is the
founder of Gittip.</em></p>
