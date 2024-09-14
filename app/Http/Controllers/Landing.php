<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;

class Landing extends Controller
{
    public function __invoke()
    {
        seo()
            ->title('Dedham Vale Driving School')
            ->description('Learn to drive with Dedham Vale Driving school. In Colchester, Clacton and Ipswich');

        return view('pages.landing');
    }
}
