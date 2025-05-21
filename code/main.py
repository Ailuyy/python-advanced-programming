from detect_and_ocr import detect_and_ocr
from calculate_grade import calculate_final_grade
import json, time

def main():
    program_start = time.time()
    img_dir = '../data/photos'
    results, elapsed = detect_and_ocr(img_dir, max_images=10, visualize=False)

    total = len(results)
    correct = sum(r['ocr_ok'] for r in results)
    accuracy = correct/total * 100 if total else 0.0
    grade = calculate_final_grade(accuracy, elapsed)
    total_runtime = time.time() - program_start
    print(f"OCR accuracy:     {correct}/{total} = {accuracy:.2f}%")
    print(f"Pipeline time:    {elapsed:.2f}s")
    print(f"Total runtime:    {total_runtime:.2f}s")
    print(f"Final grade:      {grade:.1f}")
    output = {
        "accuracy_percent": accuracy,
        "processing_time_sec": elapsed,
        "total_runtime_sec": total_runtime,
        "final_grade": grade,
        "results": results
    }
    output_path = 'results.json'
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(output, f, ensure_ascii=False, indent=2)
    print(f"Results saved to {output_path}")

if __name__ == '__main__':
    main()