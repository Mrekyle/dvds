<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;
use App\Enums\LessonTypes;

class LessonType extends Controller
{
    public function __invoke(LessonTypes $lesson)
    {
        seo()
            ->title($lesson->pageTitle())
            ->description($lesson->pageDescription());

        return view($lesson->pageView());
    }
}
