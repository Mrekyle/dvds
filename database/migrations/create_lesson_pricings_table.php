<?php

use Illuminate\Database\Migrations\Migration;
use Illuminate\Database\Schema\Blueprint;
use Illuminate\Support\Facades\Schema;

return new class extends Migration
{
    /**
     * Run the migrations.
     */
    public function up(): void
    {
        Schema::create('lesson_pricing', function (Blueprint $table) {
            $table->id();
            $table->timestamps();
            $table->char('lesson_type');
            $table->integer('duration');
            $table->float('price');
            $table->char('description');
        });
    }

    /**
     * Reverse the migrations.
     */
    public function down(): void
    {
        Schema::dropIfExists('lesson_pricings');
    }
};
