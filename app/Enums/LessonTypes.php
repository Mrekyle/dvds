<?php

declare(strict_types=1);

namespace App\Enums;

enum LessonTypes: string
{

    case Manual = 'manual';
    case Automatic = 'automatic';
    case Intensive = 'intensive';
    case Refresher = 'refresher';
    case Advanced = 'advanced';
    case Instructor = 'instructor';

    public function displayName(): string
    {
        return match ($this) {
            self::Manual => 'Manual Driving Lessons',
            self::Automatic => 'Automatic Driving Lessons',
            self::Intensive => 'Intensive Driving Lessons',
            self::Refresher => 'Refresher Driving Lessons',
            self::Advanced => 'Advanced Driving Lessons',
            self::Instructor => 'Instructor Driving Lessons',
        };
    }

    public function pageDescription(): string
    {
        return match ($this) {
            self::Manual => "Learn to drive a manual car",
            self::Automatic => "Learn to drive an automatic car",
            self::Intensive => "Learn to drive with an intensive driving course",
            self::Refresher => "Not driven in a long time, our refresher lessons are perfect for you. To get your driving confidence back.",
            self::Advanced => "Need to advance your driving skills for a job? Our advanced driving lessons are perfect for you.",
            self::Instructor => "Want to become a driving instructor and enjoy a career on the road? Our instructor driving lessons are perfect for you.",
        };
    }


    public function pageTitle(): string
    {
        return match ($this) {
            self::Manual => 'Manual Lessons',
            self::Automatic => 'Automatic Lessons',
            self::Intensive => 'Intensive Lessons',
            self::Refresher => 'Refresher Lessons',
            self::Advanced => 'Advanced Lessons',
            self::Instructor => 'Instructor Lessons',
        };
    }

    public function pageView()
    {
        return match ($this) {
            default => 'pages.lessons.' . $this->value
        };
    }
}
