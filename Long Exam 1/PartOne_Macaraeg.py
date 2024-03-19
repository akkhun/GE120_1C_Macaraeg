"""
1. When we say procedural programming, we're talking about a procedural process and when it comes to function you're supposed to have 
a specific purpose. procedural is also a type of programming na mahaba yung process and may specific process na sinusundan, functional
naman is possible to have a single purpose.

2. Git is a software that can help you share your works to other people with a faster and easier way. Sa matter ng collaborative
development, merong mga repositories sa Git in which you can share your works to other (public mo lang), then they can pull na from
there. Pwede ring sabihin na main way of helping dito is yung pagbranch. When we say branch, gagawa tayo ng panibagong file or parang
gagawa tayo ng panibagong version nung original without changing the original. Another good thing dito is pwede ang multiple branches,
meaning, pwedeng marami kayong gumagawa at the same time, and eventually pwede nyo siya imerge into one final file with all of the
changes na ginawa ninyong lahat na nagwork with the project. To summarize, yung paghelp ng Git sa Collaborative Development is yung
pag-enable sa mga tao to share and take references from other people's repositories, and to create din a platform in which you can
edit along with other people, and yung sa Version control naman, yung original work ay hindi naaapektuhan due to the branch feature and
there's an infinite room for development kasi pwedeng iedit nang iedit (di naman mawawala yung original kasi separate and branch), then
eventually imerge para makabuo ng newly developed work.


3. One should use a while loop when hindi mo alam kung ilang beses ka magloloop, kasi in a while loop, you don't know how many
loops you're going to have as long as hindi nameet yung conditions mo. One example na pwede sa field natin is yung pagkuha ng REC, 
you'll set up a condition na minimum of 1:5000 lang ang required REC, and if nameet naman to, then magbbreak na yung loop, if not,
then babalik ka ulit sa pagtraverse. Para naman sa For loop, you only use this when you know the specific number of times na you will
iterate (kung ilang beses magloloop). One example naman na related sa field ng geomatics is yung pagloop ng 


4. The Divide and Conquer paradigm "divides" and "conquers" a problem para mas madali makahanap ng solution.
A bigger problem is presented and this paradigm helps "divide" the said problem into problems na mas madali mahanapan ng solution.
In that way, we can now conquer these said sub-problems, ang ibig sabihin ng conquer dito ay to find a solution on these 
sub-problems, then once na nasolve mo na, icocorrelate or ipagsasama mo na yung solutions mo sa bawat sub-problems which 
will eventually help you solve the bigger problem na presented sa umpisa. Example siguro na big problem is traffic, then possible
sub-problems natin ("dito na pumapasok yung divide"), madaming kotse at sirang kalsada. If want mo pa idivide pwede naman pero
since this is an example, pwede na natin siya iconquer, yung solution na pwede sa madaming kotse is coding, and sa sirang kalsada
naman syempre ipaayos yung kalsada. Then we'll mix these solutions up to solve the bigger problem which is yung traffic.

5. An example that immediately popped out of my mind is yung traverse, as you manually get those distances and bearings sa fieldwork
and yung values naman na yun, you can either solve for the REC using your calculator (which can be tiring or inaccurate depending 
on a lot of factors) or iprogram (which is accurate naman if you programmed it correctly). My plan of attack in this type of example
is to first input the values na nakuha from the fieldwork. Once na nakuha na yung values, try to set a parameter na either DD
(decimal-degree) lang yung bearing or DMS (degrees-minutes-seconds) na pwedeng input, then once na nailagay na yung distance 
and bearing, I'll use some arithmetic operations sa python like (+,-,*, etc..) to compute for the lat and departure. Then I'll go
do it like sa pagadjust lang using compass rule pero in a software. Another condition pala na ilalagay ko is to put a while loop on the
input, if mali, or hindi expected yung value, then they'll have to go and input another value. I can also try to consider if magaadd 
ng new values, and kung word/letter yung idadagdag, i'll do an if-then statement tapos variable.lower = "something", parang ganyan
para lang maconsider yung sagot sa yes/no questions in any form. Then proceed lang with solving the other needed columns. With the help
of a tuple naman, i'll make sure na yung values sa lines na yun is set na. Eventually, I'll create a for loop naman para sa pagprint ng
mga values on their designated columns. After I'm done with these computations, I'll get the summation, and input na yung formula ng
LEC at REC. If mali or hindi pasok yung nakuha kong REC sa minimum requirement na sinet ni prof, then I'll have to do another traverse,
but this time, meron na kong working program na mas mapapabilis yung pagsolve sa REC.
"""
