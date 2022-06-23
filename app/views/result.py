from flask import Flask, Blueprint, render_template, request
try:
  from dictionary_files import file
except:
  from app.dictionary_files import file
import pickle
import numpy
result_bp = Blueprint("result_pb", __name__)


@result_bp.route('/POST')
def post():
  #쿼리파라미터로 들어온 값 처리
  input_text = request.args.get("input_text")
  industry_code = request.args.get('industry')
  education_code = request.args.get('education')
  experience_code = request.args.get('experience')
  job_type_code = request.args.get('job_type')
  #딕셔너리 파일 불러오기
  industry_dic = file.industry_dic
  education_dic = file.education_dic
  experience_dic = file.experience_dic
  job_type_dic = file.job_type_dic

  #딕셔너리 파일에서 위에서 들어온 쿼리 파라미터에 해당하는 값 추출
  industry = industry_dic[industry_code]
  education = education_dic[education_code]
  experience = experience_dic[experience_code]
  job_type = job_type_dic[job_type_code]
  result = "구현 전"

  with open('model.pickle', 'rb') as model_pickle:
      model = pickle.load(model_pickle)
  value = numpy.array([[int(job_type_code), int(industry_code), int(experience_code), int(education_code)]])
  result = model.predict(value)
  return render_template(
  'result.html',
  industry= industry,
  education=education,
  experience=experience,
  job_type=job_type,
  result =result)
