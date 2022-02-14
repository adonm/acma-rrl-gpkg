create view licence_detail as
select * from (select * from device_details
left join licence on device_details.LICENCE_NO = licence.LICENCE_NO) device_licence
left join site on site.SITE_ID = device_licence.SITE_ID
left join client on client.CLIENT_NO = device_licence.CLIENT_NO