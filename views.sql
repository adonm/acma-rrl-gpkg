create view licence_detail as
select * from (select * from device_details
inner join licence on device_details.LICENCE_NO = licence.LICENCE_NO) device_licence
inner join site on site.SITE_ID = device_licence.SITE_ID
inner join client on client.CLIENT_NO = device_licence.CLIENT_NO
where ABN in (91724684688,39563851304,38052249024,55028468715)
