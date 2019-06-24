
--database 생성
CREATE DATABASE campy default CHARACTER SET UTF8;






--대학교
INSERT INTO app_common_data_metadatainfo(meta_data_code,meta_data_name,meta_data_relation_code,meta_data_relation_name,upper_data_code)
VALUES('meta_universityList', '대학리스트', 'sejongUniversity', '세종대학교', '' );
INSERT INTO app_common_data_metadatainfo(meta_data_code,meta_data_name,meta_data_relation_code,meta_data_relation_name,upper_data_code)
VALUES('meta_universityList', '대학리스트', 'seoulUniversity', '서울대학교', '' );
INSERT INTO app_common_data_metadatainfo(meta_data_code,meta_data_name,meta_data_relation_code,meta_data_relation_name,upper_data_code)
VALUES('meta_universityList', '대학리스트', 'konkukUniversity', '건국대학교', '' );

--단과대학

INSERT INTO app_common_data_metadatainfo(meta_data_code,meta_data_name,meta_data_relation_code,meta_data_relation_name,upper_data_code)
VALUES('meta_collegeList', '단과대학리스트', 'sejongCollege001', '소프트웨어융합대학', 'sejongUniversity' );
INSERT INTO app_common_data_metadatainfo(meta_data_code,meta_data_name,meta_data_relation_code,meta_data_relation_name,upper_data_code)
VALUES('meta_collegeList', '단과대학리스트', 'sejongCollege002', '예체능대학', 'sejongUniversity' );
INSERT INTO app_common_data_metadatainfo(meta_data_code,meta_data_name,meta_data_relation_code,meta_data_relation_name,upper_data_code)
VALUES('meta_collegeList', '단과대학리스트', 'sejongCollege003', '전자정보통신대학', 'sejongUniversity' );
INSERT INTO app_common_data_metadatainfo(meta_data_code,meta_data_name,meta_data_relation_code,meta_data_relation_name,upper_data_code)
VALUES('meta_collegeList', '단과대학리스트', 'sejongCollege004', '단과대학없음', 'sejongUniversity' );
INSERT INTO app_common_data_metadatainfo(meta_data_code,meta_data_name,meta_data_relation_code,meta_data_relation_name,upper_data_code)
VALUES('meta_collegeList', '단과대학리스트', 'seoulCollege001', '디자인대학', 'seoulUniversity' );
INSERT INTO app_common_data_metadatainfo(meta_data_code,meta_data_name,meta_data_relation_code,meta_data_relation_name,upper_data_code)
VALUES('meta_collegeList', '단과대학리스트', 'seoulCollege002', '예체능대학', 'seoulUniversity' );
INSERT INTO app_common_data_metadatainfo(meta_data_code,meta_data_name,meta_data_relation_code,meta_data_relation_name,upper_data_code)
VALUES('meta_collegeList', '단과대학리스트', 'seoulCollege003', '컴퓨터대학', 'seoulUniversity' );
INSERT INTO app_common_data_metadatainfo(meta_data_code,meta_data_name,meta_data_relation_code,meta_data_relation_name,upper_data_code)
VALUES('meta_collegeList', '단과대학리스트', 'seoulCollege004', '단과대학없음', 'seoulUniversity' );

INSERT INTO app_common_data_metadatainfo(meta_data_code,meta_data_name,meta_data_relation_code,meta_data_relation_name,upper_data_code)
VALUES('meta_departmentList', '학과리스트', 'sejongDepart001', '컴퓨터공학과', 'sejongCollege001' );
INSERT INTO app_common_data_metadatainfo(meta_data_code,meta_data_name,meta_data_relation_code,meta_data_relation_name,upper_data_code)
VALUES('meta_departmentList', '학과리스트', 'sejongDepart002', '소프트웨어학과', 'sejongCollege001' );
INSERT INTO app_common_data_metadatainfo(meta_data_code,meta_data_name,meta_data_relation_code,meta_data_relation_name,upper_data_code)
VALUES('meta_departmentList', '학과리스트', 'sejongDepart003', '정보보호학과', 'sejongCollege001' );
INSERT INTO app_common_data_metadatainfo(meta_data_code,meta_data_name,meta_data_relation_code,meta_data_relation_name,upper_data_code)
VALUES('meta_departmentList', '학과리스트', 'sejongDepart004', '체육학과', 'sejongCollege002' );
INSERT INTO app_common_data_metadatainfo(meta_data_code,meta_data_name,meta_data_relation_code,meta_data_relation_name,upper_data_code)
VALUES('meta_departmentList', '학과리스트', 'sejongDepart005', '서양미술학과', 'sejongCollege002' );
INSERT INTO app_common_data_metadatainfo(meta_data_code,meta_data_name,meta_data_relation_code,meta_data_relation_name,upper_data_code)
VALUES('meta_departmentList', '학과리스트', 'sejongDepart006', '전자과', 'sejongCollege003' );
INSERT INTO app_common_data_metadatainfo(meta_data_code,meta_data_name,meta_data_relation_code,meta_data_relation_name,upper_data_code)
VALUES('meta_departmentList', '학과리스트', 'sejongDepart007', '자유전공학과', 'sejongCollege004' );

INSERT INTO app_common_data_metadatainfo(meta_data_code,meta_data_name,meta_data_relation_code,meta_data_relation_name,upper_data_code)
VALUES('meta_departmentList', '학과리스트', 'seoulDepart001', '컴퓨터공학과', 'seoulCollege003' );
INSERT INTO app_common_data_metadatainfo(meta_data_code,meta_data_name,meta_data_relation_code,meta_data_relation_name,upper_data_code)
VALUES('meta_departmentList', '학과리스트', 'seoulDepart002', '소프트웨어학과', 'seoulCollege003' );
INSERT INTO app_common_data_metadatainfo(meta_data_code,meta_data_name,meta_data_relation_code,meta_data_relation_name,upper_data_code)
VALUES('meta_departmentList', '학과리스트', 'seoulDepart003', '정보보호학과', 'seoulCollege003' );
INSERT INTO app_common_data_metadatainfo(meta_data_code,meta_data_name,meta_data_relation_code,meta_data_relation_name,upper_data_code)
VALUES('meta_departmentList', '학과리스트', 'seoulDepart004', '해킹학과', 'seoulCollege003' );
INSERT INTO app_common_data_metadatainfo(meta_data_code,meta_data_name,meta_data_relation_code,meta_data_relation_name,upper_data_code)
VALUES('meta_departmentList', '학과리스트', 'seoulDepart005', '시각디자인학과', 'seoulCollege001' );
INSERT INTO app_common_data_metadatainfo(meta_data_code,meta_data_name,meta_data_relation_code,meta_data_relation_name,upper_data_code)
VALUES('meta_departmentList', '학과리스트', 'seoulDepart006', '산업디자인학과', 'seoulCollege001' );
INSERT INTO app_common_data_metadatainfo(meta_data_code,meta_data_name,meta_data_relation_code,meta_data_relation_name,upper_data_code)
VALUES('meta_departmentList', '학과리스트', 'seoulDepart007', '체육특기학과', 'seoulCollege002' );

--이수구분
INSERT INTO app_common_data_metadatainfo(meta_data_code,meta_data_name,meta_data_relation_code,meta_data_relation_name,upper_data_code)
VALUES('meta_completionDivision', '이수구분리스트', 'sejongCompletionDivision001', '전공필수', 'sejongUniversity' );
INSERT INTO app_common_data_metadatainfo(meta_data_code,meta_data_name,meta_data_relation_code,meta_data_relation_name,upper_data_code)
VALUES('meta_completionDivision', '이수구분리스트', 'sejongCompletionDivision002', '전공선택', 'sejongUniversity' );
INSERT INTO app_common_data_metadatainfo(meta_data_code,meta_data_name,meta_data_relation_code,meta_data_relation_name,upper_data_code)
VALUES('meta_completionDivision', '이수구분리스트', 'sejongCompletionDivision003', '중핵필수', 'sejongUniversity' );
INSERT INTO app_common_data_metadatainfo(meta_data_code,meta_data_name,meta_data_relation_code,meta_data_relation_name,upper_data_code)
VALUES('meta_completionDivision', '이수구분리스트', 'sejongCompletionDivision004', '중핵선택', 'sejongUniversity' );
INSERT INTO app_common_data_metadatainfo(meta_data_code,meta_data_name,meta_data_relation_code,meta_data_relation_name,upper_data_code)
VALUES('meta_completionDivision', '이수구분리스트', 'sejongCompletionDivision005', '자유교양', 'sejongUniversity' );
INSERT INTO app_common_data_metadatainfo(meta_data_code,meta_data_name,meta_data_relation_code,meta_data_relation_name,upper_data_code)
VALUES('meta_completionDivision', '이수구분리스트', 'sejongCompletionDivision006', '기초교양', 'sejongUniversity' );

--영역
INSERT INTO app_common_data_metadatainfo(meta_data_code,meta_data_name,meta_data_relation_code,meta_data_relation_name,upper_data_code)
VALUES('meta_domain', '영역리스트', 'sejongDomain001', '사회와가치', 'sejongUniversity' );
INSERT INTO app_common_data_metadatainfo(meta_data_code,meta_data_name,meta_data_relation_code,meta_data_relation_name,upper_data_code)
VALUES('meta_domain', '영역리스트', 'sejongDomain001', '과학과기술', 'sejongUniversity' );
INSERT INTO app_common_data_metadatainfo(meta_data_code,meta_data_name,meta_data_relation_code,meta_data_relation_name,upper_data_code)
VALUES('meta_domain', '영역리스트', 'sejongDomain001', '인성과도덕', 'sejongUniversity' );
INSERT INTO app_common_data_metadatainfo(meta_data_code,meta_data_name,meta_data_relation_code,meta_data_relation_name,upper_data_code)
VALUES('meta_domain', '영역리스트', 'sejongDomain001', '쓰기와말하기', 'sejongUniversity' );


--과목정보

--세종대학교
INSERT INTO app_common_data_subjectinfo(ID,university_name,subject_code,subject_name,subject_completion_division,subject_area,subject_credit)
VALUES(1,'세종대학교', 'E1000', 'C언어', '전공필수', '', 3.0);
INSERT INTO app_common_data_subjectinfo(ID,university_name,subject_code,subject_name,subject_completion_division,subject_area,subject_credit)
VALUES(2,'세종대학교', 'E1001', 'JAVA', '전공선택', '', 2.0);
INSERT INTO app_common_data_subjectinfo(ID,university_name,subject_code,subject_name,subject_completion_division,subject_area,subject_credit)
VALUES(3,'세종대학교', 'E1002', '자료구조', '전공필수', '', 4.0);
INSERT INTO app_common_data_subjectinfo(ID,university_name,subject_code,subject_name,subject_completion_division,subject_area,subject_credit)
VALUES(4,'세종대학교', 'E1003', '알고리즘', '전공필수', '', 4.0);
INSERT INTO app_common_data_subjectinfo(ID,university_name,subject_code,subject_name,subject_completion_division,subject_area,subject_credit)
VALUES(5,'세종대학교', 'E1004', '운영체제', '전공필수', '', 3.0);
INSERT INTO app_common_data_subjectinfo(ID,university_name,subject_code,subject_name,subject_completion_division,subject_area,subject_credit)
VALUES(6,'세종대학교', 'F1000', '세종리더십', '중핵필수', '사회와가치', 2.0);
INSERT INTO app_common_data_subjectinfo(ID,university_name,subject_code,subject_name,subject_completion_division,subject_area,subject_credit)
VALUES(7,'세종대학교', 'F1002', '과학과기술입문', '중핵필수선택', '과학과기술', 2.0);
INSERT INTO app_common_data_subjectinfo(ID,university_name,subject_code,subject_name,subject_completion_division,subject_area,subject_credit)
VALUES(8,'세종대학교', 'F1003', '세종사회봉사', '중핵필수', '', 1.0);





