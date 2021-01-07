from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, PasswordField, SelectField, BooleanField, TextAreaField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from sim.models import Tmahasiswa
from flask_login import current_user
from flask_wtf.file import FileField, FileAllowed
import random


class mahasiswa_F(FlaskForm):
    npm= StringField('NPM',validators=[DataRequired(), Length(min=10, max=15)])
    nama= StringField('Nama',validators=[DataRequired()])
    email= StringField('Email',validators=[DataRequired(), Email()])
    password= PasswordField('Password',validators=[DataRequired(), Length(min=6, max=15)])
    konf_pass= PasswordField('Konfirmasi Password',validators=[DataRequired(), EqualTo('password')])
    kelas= StringField('Kelas',validators=[DataRequired()])
    alamat = TextAreaField('Alamat')
    submit= SubmitField('Tambah')

    ##### validasi npm#####
    def validate_npm(self,npm):
        ceknpm=Tmahasiswa.query.filter_by(npm=npm.data).first()
        if ceknpm:
            raise ValidationError('NPM Sudah Terdaftar!')
    
    ### validasi email ###
    def validate_email(self, email):
        cekemail=Tmahasiswa.query.filter_by(email=email.data).first()
        if cekemail:
            raise ValidationError('Email Telah Digunakan!')

class loginmahasiswa_F(FlaskForm):
    npm= StringField('NPM',validators=[DataRequired()])
    password= PasswordField('Password',validators=[DataRequired()])
    submit= SubmitField('Login')



class editmahasiswa_F(FlaskForm):
    npm= StringField('NPM',validators=[DataRequired(), Length(min=10, max=15)])
    nama= StringField('Nama',validators=[DataRequired()])
    email= StringField('Email',validators=[DataRequired(), Email()])
    password= PasswordField('Password',validators=[DataRequired(), Length(min=6, max=15)])
    konf_pass= PasswordField('Konfirmasi Password',validators=[DataRequired(), EqualTo('password')])
    kelas= StringField('Kelas',validators=[DataRequired()])
    alamat = TextAreaField('Alamat')
    foto=FileField('Ubah Foto Profil',validators=[FileAllowed(['jpg','png'])])
    submit= SubmitField('Ubah Data')

    ##### validasi npm#####
    def validate_npm(self,npm):
        if npm.data !=current_user.npm:
            ceknpm=Tmahasiswa.query.filter_by(npm=npm.data).first()
            if ceknpm:
                raise ValidationError('NPM Sudah Terdaftar!')
        
    ### validasi email ###
    def validate_email(self, email):
        if email.data !=current_user.email:
            cekemail=Tmahasiswa.query.filter_by(email=email.data).first()
            if cekemail:
                raise ValidationError('Email Telah Digunakan!')


class pengaduan_F(FlaskForm):
    subjek= StringField('Subjek',validators=[DataRequired()])
    kategori= SelectField(u'Kategori Pengaduan', choices=[('Administrasi','Pelayanan Administrasi'),('Fasilitas','Fasilitas'),('Dosen','Dosen')], validators=[DataRequired()])
    detail_pengaduan = TextAreaField('Detail Pengaduan', validators=[DataRequired()])
    submit= SubmitField('Kirim')

class editpengaduan_F(FlaskForm):
    subjek= StringField('Subjek',validators=[DataRequired()])
    kategori= SelectField(u'Kategori Pengaduan', choices=[('Administrasi','Pelayanan Administrasi'),('Fasilitas','Fasilitas'),('Dosen','Dosen')], validators=[DataRequired()])
    detail_pengaduan = TextAreaField('Detail Pengaduan', validators=[DataRequired()])
    submit= SubmitField('Ubah')


