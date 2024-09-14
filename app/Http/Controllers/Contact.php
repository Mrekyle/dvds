<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;

class Contact extends Controller
{
    public function __invoke()
    {
        seo()
            ->title("DVD's: Get In Touch")
            ->description("get in touch with us to start your journey on the road");

        return view('pages.contact');
    }
}
