<?php

use Illuminate\Support\Facades\Route;

Route::get('/', \App\Http\Controllers\Landing::class)->name('home');
Route::get('about', \App\Http\Controllers\About::class)->name('about');
Route::get('contact', \App\Http\Controllers\Contact::class)->name('contact');
Route::get('instructor', \App\Http\Controllers\Instructors::class)->name('instructor');
Route::get('lesson/{lesson}', \App\Http\Controllers\LessonType::class)->name('lesson');
Route::get('services/{service}', \App\Http\Controllers\Service::class)->name('services');

Route::view('dashboard', 'dashboard')
    ->middleware(['auth', 'verified'])
    ->name('admin.dashboard');

Route::view('profile', 'profile')
    ->middleware(['auth'])
    ->name('admin.profile');

require __DIR__ . '/auth.php';
