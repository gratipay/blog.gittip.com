---
title: Payday Rewrite Optimizes Credit Card Fees
dateline: August 14, 2014, 4:19 pm
layout: page
---

<p>Every Thursday, we charge credit cards, shuffle the money around inside
Gittip, and deposit money to bank accounts. We call this &#8220;payday.&#8221;
It&#8217;s really the core of Gittip, and the process hasn&#8217;t been
substantially refactored since we launched over two years ago.</p>

<p>For the past two months we&#8217;ve been working on a <a
href="https://github.com/gittip/www.gittip.com/issues/2508">rewrite</a> of the
payday algorithm that addresses a number of under-the-hood issues. Payday is now
safer and faster.</p>

<p>The most visible user-facing change is that now, if you&#8217;re both giving
and receiving money on Gittip, we&#8217;ll only charge your credit card for the
difference. Before, we were charging you the whole amount of your gifts even if
you were also receiving money, which was confusing and also wasted money in
credit card fees.</p>

<p>This has been a significant engineering effort for our team, which is still
very much in the bootstrapping phase. In fact, we think of ourselves as &#8220
;double-bootstrapping,&#8221; since we&#8217;re trying to <a
href="https://www.gittip.com/Gittip/">fund ourselves</a> on the very platform
we&#8217;re building. In particular I&#8217;d like to thank <a
href="https://www.gittip.com/Changaco/">Changaco</a> for all of his hard work on
this payday rewrite and many other parts of Gittip.</p>

<p>Now would be a good time to double-check your <a
href="https://www.gittip.com/about/me/history/">history page</a> on Gittip. If
you see something wrong or confusing, please let us know either privately by
emailing <a href="mailto:support@gittip.com">support@gittip.com</a>, or publicly
on <a href="https://twitter.com/Gittip">Twitter</a> or <a
href="https://github.com/gittip/www.gittip.com/issues/new">GitHub</a>.</p>

<p>Thanks for using Gittip!</p><hr>

<p><em>Chad Whitacre is the founder of Gittip.</em></p>
