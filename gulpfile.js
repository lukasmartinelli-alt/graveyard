var gulp = require('gulp');
var jshint = require('gulp-jshint');
var sass = require('gulp-sass');

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
    gulp.watch('{server,client}/**/*.js', ['lint']);
});
