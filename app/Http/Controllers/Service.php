<?php

namespace App\Http\Controllers;

use App\Enums\Services as Services;
use Illuminate\Http\Request;

class Service extends Controller
{
    public function __invoke(Services $service)
    {
        seo()
            ->title("DVD's: " . $service->pageTitle())
            ->description("Our Services");

        return view($service->pageView());
    }
}
