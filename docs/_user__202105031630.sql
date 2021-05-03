INSERT INTO public."user" (id,"password","name",phone_number,status,email,"role",is_deleted) VALUES
	 (23,'pbkdf2:sha256:150000$35SbkMYp$fd4cc8aa09e8d3e4d257f9b221365af962be4a9e42d100d90fa5ef7e1d349529','hhhh','01000000000','','b@gmail.com','USER',0),
	 (4,'pbkdf2:sha256:150000$k5jbvgEh$d9486cc158227e51d0847e53085afd0b065c46e16936b47f8ecfa2501e291c67','멍이나물','01092129214','','a@gmail.com','USER',1),
	 (1,'1234','홍길동','01012345678',NULL,'h@gmail.com','ADMIN',0),
	 (2,'1234','임꺽정','01098765432',NULL,'l@gmail.com','ADMIN',0),
	 (22,'pbkdf2:sha256:150000$IVa9c4fC$a2cd6e7a18616ea558bfe398460981e2d93df8fe5e30119a58fe6db8a7eb0520','멍이나물','01012345678','','j@naver.com','USER',0);