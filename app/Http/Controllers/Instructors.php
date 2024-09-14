<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;

class Instructors extends Controller
{
    public function __invoke()
    {
        seo()
            ->title("DVD's: Meet the Instructors")
            ->description("Meet the Dedham Vale Driving School Instructors");

        return view('pages.instructors');
    }
}
