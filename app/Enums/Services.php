<?php

declare(strict_types=1);

namespace App\Enums;

enum Services: string
{
    case WeeklyLessons = 'weekly-lessons';
    case Automatic = 'automatic-lessons';
    case Intensive = 'intensive-lessons';
    case Refresher = 'refresher-lessons';
    case TestAndTheory = 'test-and-theory';
    case Instructor = 'instructor-training';

    public function displayName(): string
    {
        return match ($this) {
            self::WeeklyLessons => 'Weekly Lessons',
            self::Automatic => 'Automatic Lessons',
            self::Intensive => 'Intensive Lessons',
            self::Refresher => 'Refresher Lessons',
            self::TestAndTheory => 'Test and Theory Training',
            self::Instructor => 'Driving Instructor Training',
        };
    }

    public function pageTitle(): string
    {
        return match ($this) {
            self::WeeklyLessons => 'Weekly Driving Lessons',
            self::Automatic => 'Automatic Driving Lessons',
            self::Intensive => 'Intensive Driving Lessons',
            self::Refresher => 'Refresher Driving Lessons',
            self::TestAndTheory => 'Test and Theory Training',
            self::Instructor => 'Driving Instructor Training',
        };
    }

    public function pageDescription(): string
    {
        return match ($this) {
            self::WeeklyLessons => "Learn to drive a manual car",
            self::Automatic => "Learn to drive an automatic car",
            self::Intensive => "Learn to drive with an intensive driving course",
            self::Refresher => "Not driven in a long time, our refresher lessons are perfect for you. To get your driving confidence back.",
            self::TestAndTheory => "Nervous about the test? Or the theory test. Well we have you covered.",
            self::Instructor => "Want to become a driving instructor and enjoy a career on the road? Our instructor driving lessons are perfect for you.",
        };
    }

    public function pageView(): string
    {
        return match ($this) {
            default => 'pages.lessons.' . $this->value
        };
    }
}
