use publications;

#Challenge1
create table challenge_1
select titles.title, titles.title_id, titleauthor.au_id, concat(authors.au_fname, " ", authors.au_lname) as complete_name, 
pub_name
from titles
left join publishers
on titles.pub_id = publishers.pub_id
left join titleauthor
on titles.title_id = titleauthor.title_id
left join authors
on authors.au_id = titleauthor.au_id
;

select *
from challenge_1;

#Challenge2
select au_id as author_ID, complete_name, pub_name as publisher, count(distinct(title_id)) as title_count
from challenge_1
group by author_ID, complete_name, publisher
order by title_count DESC
;

#Challenge3
#Challenge3
select titleauthor.au_id as author_ID, concat(authors.au_fname, " ", authors.au_lname) as complete_name, 
sum(sales.qty) as units_sold
from titles
left join sales
on sales.title_id = titles.title_id
left join titleauthor
on titles.title_id = titleauthor.title_id
left join authors
on authors.au_id = titleauthor.au_id
group by author_ID
order by units_sold DESC
limit 3
;

#Challenge4
#Solo dejas de escribir el limit3