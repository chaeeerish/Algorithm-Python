-- 모든 컬럼 보기
select * from vila_list limit 10;

-- 특정 컬럼만 보기
select price, con_year from vila_list limit 10;

-- 정렬하기 (limit 보다는 위에)
select * from apt_list order by price limit 100;
select * from apt_list order by price desc limit 100;
select * from apt_list order by year, month, day limit 100;

-- 특정 열들의 개수를 세기
select count(*) from apt_list;

-- 특정 항목들의 개수를 세기
select dong, count(*) from apt_list group by dong;
select year, count(*) from apt_list group by year;

-- 중복을 제거해주는 group by
select year from apt_list group by year;

-- 특정 조건의 행들만 검색하기
select * from apt_list where dong='삼성동' limit 100;
select * from apt_list where dong='삼성동' and day=1 limit 1;

-- case when, else
select price, year, month, day, nm
       ,case when price <= 10000 then '1억 이하'
            when price <= 30000 then '1억~3억 이하'
            else '기타 표현 내용'
        end
from apt_list, limit 100;

-- 아파트 이름에 '자이'가 포함되는 경우만 출력하고 싶다면?
select * from apt_list where rm like '%자이%' limit 100;

-- 아파트 이름에 '자이'가 포함되지 않는 경우만 출력하고 싶다면?
select * from apt_list where rm not like '%자이%' limit 100;

-- 서브 쿼리
select *
from (
    select dong, count(*) cnt
    from apt_list
    group by dong
     )
where cnt > 100;

select a.*
    ,case when cnt < 200 then '200 미만 거래 지역' else '200 이상 거래 지역' end
from (
    select dong, count(*) cnt
    from apt_list
    group by dong
     ) a;

-- 여러 테이블의 정보를 결합하는 Join
select a.dong, a.nm, a.size, a.price, b.gu, b.dong
from apt_list a, area_cd
where a.area_cd=b.area_cd limit 5;

-- 정보가 없어도 출력하는 Outer Join
select a.gu, a.dong, b.nm, b.size, b.price
from area_cd a
left outer join apt_list b
on a.area_cd = b.area_cd and b.con_year = 2020
limit 50;

-- Sum/Min/Max/Avg
select sum(price), min(price), max(price), avg(price) from apt_list where year=2020;
select dong, sum(price), min(price), max(price), avg(price) from apt_list group by dong;