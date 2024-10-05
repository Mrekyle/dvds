<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;
use Illuminate\View\View;

class DrivingLessonController extends Controller
{
    public function __invoke(): View
    {
        seo()
            ->title("DVD's: Our Driving Lessons")
            ->description("Find out what is right for you. To get you on the road safely");

        return view('pages.driving-lessons');
    }
}
