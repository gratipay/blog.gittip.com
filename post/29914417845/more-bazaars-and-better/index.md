---
title: More Bazaars and Better
dateline: August 21, 2012, 4:06 pm
layout: page
---

<p>I&#8217;m teaching a <a href="http://www.whit537.org/courses/web-
development-101/">course</a> this Fall entitled <em>Web Development 101: Hacker
Theory and Practice</em>, with the <a
href="http://saxifrageschool.org/">Saxifrage School</a>. For the theory side of
the course, we&#8217;re going to read <em><a
href="http://www.catb.org/esr/writings/cathedral-bazaar/">The Cathedral and the
Bazaar</a></em> (<em>CatB</em>) by Eric Raymond (ESR). I started my programming
career in late 1999, soon after the first edition was published (the core essay
dates from 1997). The second edition landed in 2001, soon after the dot-com
bubble burst. Until reading the book, I actually didn&#8217;t realize the
&#8220;open source&#8221; <a href="http://opensource.org/">brand</a> was
invented as <a href="http://www.catb.org/esr/writings/cathedral-bazaar/hacker-
revenge/ar01s05.html">late</a> as 1998. I accidentally grew up as a hacker
right alongside the open source movement.</p>

<p>I finished reading <em>CatB</em> a couple nights ago, in time for Poul-
Henning Kamp&#8217;s ranting <a
href="http://queue.acm.org/detail.cfm?id=2349257">lament</a> for the Cathedral
(discussed <a href="http://news.ycombinator.com/item?id=4407188">extensively</a>
on Hacker News). I&#8217;m a bit of a PHK fanboy, to be honest, having used
FreeBSD and especially <a
href="http://www.freebsd.org/cgi/man.cgi?query=jail">jail(8)</a> for my first
years as a hacker (now it&#8217;s mostly Mac OS and Heroku). I used his beerware
license for some <a
href="http://www.zetadev.com/svn/public/svneol/trunk/README">early</a> projects.
However, I don&#8217;t think it&#8217;s smart to fight with reality, and 50% of
the population is below average. To me, the transcendent wonder of the bazaar is
in including <em>all</em> contributors and <em>all</em> contributions in
something bigger than the sum of its parts.</p>

<p>I think we need more bazaars, and better ones. We need people with
PHK&#8217;s taste to somehow figure out how to organize and direct the energy of
the supposedly unwashed masses. I admire Linus for having done this with Linux
(<a href="http://article.gmane.org/gmane.comp.version-
control.git/57918">prickly</a> though he might be). I admire Guido for having
done this with Python. And to an extent, I admire Jimmy Wales for having done
this with Wikipedia.</p><h4>Wikipedia</h4>

<p><em>CatB</em> concludes as follows:</p>

<blockquote>

<div>

<p>I expect the open-source movement to have essentially won its point about
software within three to five years (that is, by 2003–2005). Once that is
accomplished, and the results have been manifest for a while, they will become
part of the background culture of non-programmers. At <em>that</em> point it
will become more appropriate to try to leverage open-source insights in wider
domains.</p></div></blockquote>

<p>I see Wikipedia as the first non-programming open source success. Based on
the following <a
href="http://en.wikipedia.org/wiki/File:EnwikipediaArt.PNG">graph</a> of
Wikipedia&#8217;s growth, ESR&#8217;s prediction seems to have been spot on:
Wikipedia really started to take off between 2003 and 2005.</p>

<p><img alt="image"
src="http://media.tumblr.com/tumblr_m948r6xosz1rn81gb.png"/></p>

<p>Wikipedia is interesting both for what it is&#8212;the free encyclopedia that
anyone can edit&#8212;and for how it is managed: <a
href="http://meta.wikimedia.org/wiki/Main_Page">openly</a>. Not only can anyone
edit Wikipedia, anyone can <a
href="http://strategy.wikimedia.org/wiki/Main_Page">edit the Wikimedia
Foundation</a> itself. That&#8217;s new. That&#8217;s big. It&#8217;s a best-of-
both-worlds mashup between a corporation and a government. It&#8217;s nominally
a charity, but the 501(c)(3) is a red herring: the preponderance of
Wikimedia&#8217;s mass is in the community of people who are <em>not</em> on <a
href="http://wikimediafoundation.org/wiki/File:501(c)3_Letter.png">WIKIMEDIA
FOUNDATION INC</a>'s payroll.</p>

<p>Now, imagine if Jimmy Wales had Steve Jobs&#8217; taste. Imagine if Wikipedia
weren&#8217;t painfully ugly. Imagine if the editing experience were delightful.
Yes, there is Project Athena. To be honest, <a
href="http://upload.wikimedia.org/wikipedia/commons/5/50/Wikimania_-_2012_-
_Athena_Project.pdf">early signs</a> (PDF) leave me underwhelmed:</p>

<p><img alt="image"
src="http://media.tumblr.com/tumblr_m94ackqwPk1rn81gb.jpg"/></p>

<p>Imagine if the GitHub team were building Wikipedia. The tagging interface
would be <em>awesome</em>, if they decided we needed it at all.</p><h4>Making Good</h4>

<p>ESR is <a href="http://www.catb.org/esr/writings/cathedral-bazaar/hacker-
revenge/ar01s09.html">prescient</a> here as well:</p>

<blockquote>

<div>

<p>I believe the problem for 2001 and later is whether we can grow enough to
meet (and <em>exceed</em>!) the interface-design quality standard set by the
Macintosh, combining that with the virtues of the traditional Unix way.</p></div></blockquote>

<p>However, he turns out to have been too optimistic:</p>

<blockquote>

<div>

<p>As of mid-2000, help may be on the way from the inventors of the Macintosh!
Andy Hertzfeld and other members of the original Macintosh design team have
formed an open-source company called Eazel with the explicit goal of bringing
the Macintosh magic to Linux.</p></div></blockquote>

<p>ESR actually <a href="http://www.catb.org/esr/writings/cathedral-bazaar
/hacker-revenge/ar01s09.html">speculated</a> that Apple itself might &#8220;go
open&#8221; with Mac OS X, because in his <a
href="http://www.catb.org/esr/writings/cathedral-bazaar/magic-
cauldron/ar01s10.html#id2762774">view</a> &#8220;open-source peer review is the
only scalable method for achieving high reliability and quality.&#8221; Well, I
daresay that Google and Amazon and Facebook have demonstrated this to be false.
These companies depend on open source software, yes. But there is surely a great
deal of proprietary work that is essential to their reliability and quality. And
far from &#8220;go[ing] open&#8221; with Mac OS, Apple did the opposite. It
wrapped FreeBSD in a heavy coat of proprietary code, and captured the
lion&#8217;s share of the <a href="http://paulgraham.com/mac.html">hacker
laptop</a> market. Ubuntu&#8217;s user experience is nothing compared to Mac
OS&#8217;s. Apple then used the iOS variant of Mac OS to basically create the
mobile market as we know it <em>ex nihilo</em>, boosting its consumer laptop
sales in the process. Meanwhile, <a
href="http://en.wikipedia.org/wiki/Eazel">Eazel</a> folded in 2001, and after
a few more years trying to <a href="http://www.osafoundation.org/">make good</a>
on ESR&#8217;s vision, <a
href="http://en.wikipedia.org/wiki/Andy_Hertzfeld">Andy Hertzfeld</a> went to
Google in 2005, where he remains to this day. ESR&#8217;s poster children are
now bywords and also-rans: Netscape, VA Linux, SourceForge, RedHat. Mozilla is
basically kept alive by Google, for it&#8217;s own strategic purposes. And then
Google went and built Chrome anyway. Sometimes it feels to me like open source
is less of a revolutionary than a lapdog.</p>

<p>What happened? Why are our best people building Google and Facebook and
GitHub, and not Wikipedia? Or rather: Why aren&#8217;t Google and Facebook and
GitHub open projects like Wikipedia? Simple: It&#8217;s not yet economically
rational for the world&#8217;s top talent to work on open projects. But I think
it could and should be.</p>

<p>If I don&#8217;t like the direction Project Athena is going, I should get
involved in the Wikimedia movement and &#8220;edit&#8221; it myself. Right? In a
way, I see myself doing that with <a
href="https://www.gittip.com/about/">Gittip</a>. I want Gittip to shift the
economy towards open projects like Wikipedia. Why? Because I was raised in the
bazaar. I love working together as free equals, rather than being someone
else&#8217;s cog. Though chains be of gold, they are chains all the same.</p>

<p>Fifty years from now, I want most economic activity to happen in the open.
That&#8217;s a dream. I want <a href="http://blog.gittip.com/post/26350459746
/the-first-open-company">open companies</a>, with open governments to
follow.</p>

<p>If you want to see this too, consider joining Gittip, and funding someone
who <a href="https://www.gittip.com/on/github/wikimedia/">works on
Wikipedia</a>. While you&#8217;re at it, why not fund the people who <a
href="https://www.gittip.com/on/github/github/">build GitHub</a>? Would they
open up their company, if we made it economically rational? Maybe some of them
would even go help out on Wikipedia.</p>

<p>&#8212;&#8212;&#8212;&#8212;</p>

<p><em><a href="https://www.gittip.com/whit537/">Chad Whitacre</a> is the
founder of <a href="https://www.gittip.com/">Gittip</a>.</em></p>
