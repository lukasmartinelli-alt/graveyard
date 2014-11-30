var gulp = require('gulp');
var jshint = require('gulp-jshint');
var sass = require('gulp-sass');
var livereload = require('gulp-livereload');

gulp.task('sass', function() {
    return gulp.src('client/scss/*.scss')
        .pipe(sass())
        .pipe(gulp.dest('client/css'));
});

gulp.task('lint', function() {
    return gulp.src('{server,client}/**/*.js')
        .pipe(jshint())
        .pipe(jshint.reporter('default'));
});

gulp.task('watch', function() {
    livereload.listen();
    gulp.watch('client/scss/*.scss', ['sass']).on('change', livereload.changed);
    gulp.watch('{server,client}/**/*.js', ['lint']);
    gulp.watch('client/*.html').on('change', livereload.changed);
});
