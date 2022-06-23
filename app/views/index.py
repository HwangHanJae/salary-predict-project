from flask import Flask, Blueprint, render_template
try:
  from dictionary_files import file
except:
  from app.dictionary_files import file

index_bp = Blueprint('index_bp', __name__)

@index_bp.route('/')
def index():
  industry_items = file.industry_dic.items()
  education_items = file.education_dic.items()
  experience_items = file.experience_dic.items()
  job_type_items = file.job_type_dic.items()
  return render_template(
    'index.html',
    industry_items=industry_items,
    education_items = education_items,
    experience_items = experience_items,
    job_type_items= job_type_items)