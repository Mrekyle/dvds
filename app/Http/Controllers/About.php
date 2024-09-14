<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;

class About extends Controller
{
    public function __invoke()
    {
        seo()
            ->title("DVD's: About")
            ->description("Learn about Dedham Vale Driving School");

        return view('pages.about');
    }
}
