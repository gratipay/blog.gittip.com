---
title: Errors in Team Distributions Last Week
dateline: May 14, 2014, 4:04 pm
layout: page
---

<p>Gittip&#8217;s <a href="https://www.gittip.com/about/teams/">Teams</a>
feature enables the distribution of funds each week among members of a team.
During last week&#8217;s payday, two bugs in the algorithm for distributing team
funds led to overpayments to 55 members across 21 teams, totaling $141.34. Most
of this was for the Gittip and Aspen teams: $124.56 (88%) to 13 members (62%).
Additionally, funds (less than $2) were not distributed at all to eight members
across three teams.</p>

<p>The payday algorithm runs in three loops: payin, pachinko, and payout.
Pachinko is where the team distribution happens. Payday crashed twice during the
pachinko loop due to bugs in the pachinko algorithm. After the second crash, we
decided to skip the pachinko loop entirely and proceed directly to the payout
loop. We took this decision on the understanding that the dollar amounts
involved with teams is relatively small, so the risk of needing to do a major
correction was low, and we were under time pressure to submit payouts for the
day to our processor, Balanced Payments.</p>

<p>Since most of the money involved in the error was for the Gittip and Aspen
teams and the effect on other teams was so small, we decided to let the
overpayments stand. This amounts to an extra payment from the teams in question
to their members.</p>

<p>For further details please see <a
href="https://github.com/gittip/www.gittip.com/issues/2362">this GitHub
issue</a>.</p>

<p>Sorry for the error. If you have any questions or concerns, please get in
touch on <a href="https://twitter.com/Gittip">Twitter</a> or <a
href="irc://irc.freenode.net/#gittip">IRC</a> or <a
href="mailto:support@gittip.com">email</a>.</p>
