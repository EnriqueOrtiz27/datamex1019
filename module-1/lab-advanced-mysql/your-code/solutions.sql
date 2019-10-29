use publications; 
#Challenge1

#step 1
use publications;
create temporary table step_1
select titles.title_id, authors.au_id, 
titles.price*sales.qty*(titles.royalty/100)*(titleauthor.royaltyper / 100) as royalty
from titles
inner join titleauthor
on titles.title_id = titleauthor.title_id
inner join sales
on sales.title_id = titles.title_id
inner join authors
on authors.au_id = titleauthor.au_id

#Step 2; note that I used a table created in Step 1
create temporary table step_2
select title_id, au_id, sum(royalty) as sum_royalty
from step_1
group by title_id, au_id;

#step 3
select distinct(au_id) as authorID, sum(sum_royalty) as total_author
from step_2
group by au_id
;


#Challenge2

#Challenge2

use publications;
select distinct(au_id) as authorID, sum(sum_royalty) as total_author
from 
(select title_id, au_id, sum(royalty) as sum_royalty
from
(select titles.title_id, authors.au_id, 
titles.price*sales.qty*(titles.royalty/100)*(titleauthor.royaltyper / 100) as royalty
from titles
inner join titleauthor
on titles.title_id = titleauthor.title_id
inner join sales
on sales.title_id = titles.title_id
inner join authors
on authors.au_id = titleauthor.au_id
group by title_id, au_id) step_1
group by au_id) step_2
;


#Challenge3

use publications;
create table table_challenge_3 
select distinct(au_id) as authorID, sum(sum_royalty) as total_author
from step_2
group by au_id;


