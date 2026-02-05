-- 코드를 작성해주세요
select a.ITEM_ID ITEM_ID, ITEM_NAME, RARITY
from ITEM_INFO a
    inner join ITEM_TREE b on a.ITEM_ID=b.ITEM_ID
where PARENT_ITEM_ID in (SELECT ITEM_ID FROM ITEM_INFO WHERE RARITY = 'RARE')
order by ITEM_ID desc